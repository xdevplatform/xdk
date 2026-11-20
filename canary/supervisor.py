#!/usr/bin/env python3
"""
Unified Multi-SDK Continuous Canary Supervisor for XDK.

Runs and supervises the Java (`xdk-java`) and C# (`xdk-csharp`) continuous SDK canary environments
either as a single verification pass (`--once`) or as an always-on background service (`--daemon`)
exposing aggregated `/health`, `/status`, and Prometheus `/metrics` endpoints.

Usage:
  # Run one full multi-SDK canary verification pass:
  python3 canary/supervisor.py --once

  # Run continuously as an always-on fleet canary daemon on port 8780:
  python3 canary/supervisor.py --daemon --interval-seconds 30 --port 8780
"""

from __future__ import annotations

import argparse
import concurrent.futures
import http.server
import json
import os
import shutil
import signal
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional


def find_executable(name: str, fallbacks: List[str]) -> str:
    found = shutil.which(name)
    if found:
        return found
    for candidate in fallbacks:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    raise FileNotFoundError(f"Could not find `{name}` on PATH or in {fallbacks}")


def build_java_classpath(java_dir: Path, mvn_bin: str, env: Dict[str, str]) -> str:
    cp_file = java_dir / "target" / "canary-test-cp.txt"
    subprocess.run(
        [
            mvn_bin,
            "-q",
            "test-compile",
            "dependency:build-classpath",
            "-DincludeScope=test",
            f"-Dmdep.outputFile={cp_file}",
        ],
        cwd=str(java_dir),
        env=env,
        check=True,
    )
    dep_cp = cp_file.read_text(encoding="utf-8").strip()
    parts = [
        str(java_dir / "target" / "test-classes"),
        str(java_dir / "target" / "classes"),
    ]
    if dep_cp:
        parts.append(dep_cp)
    return os.pathsep.join(parts)


def build_csharp_examples(csharp_dir: Path, dotnet_bin: str, env: Dict[str, str]) -> Path:
    proj = csharp_dir / "examples" / "Xdk.Examples" / "Xdk.Examples.csproj"
    subprocess.run(
        [dotnet_bin, "build", str(proj), "-c", "Release", "--nologo", "-v", "q"],
        cwd=str(csharp_dir),
        env=env,
        check=True,
    )
    dll = csharp_dir / "examples" / "Xdk.Examples" / "bin" / "Release" / "net8.0" / "Xdk.Examples.dll"
    if not dll.is_file():
        raise FileNotFoundError(f"Expected compiled assembly at {dll}")
    return dll


def parse_last_json_line(stdout: str) -> Dict[str, Any]:
    for line in reversed(stdout.splitlines()):
        stripped = line.strip()
        if stripped.startswith("{") and stripped.endswith("}"):
            try:
                data = json.loads(stripped)
                if "healthy" in data and "probes" in data:
                    return data
            except json.JSONDecodeError:
                continue
    raise RuntimeError(f"Did not find CanarySnapshot JSON in output:\n{stdout}")


def run_once_mode(
    sdks: List[str],
    java_dir: Path,
    csharp_dir: Path,
    java_bin: str,
    mvn_bin: str,
    dotnet_bin: str,
    live: bool,
    env: Dict[str, str],
) -> int:
    tasks: Dict[str, List[str]] = {}
    if "java" in sdks:
        cp = build_java_classpath(java_dir, mvn_bin, env)
        cmd = [java_bin, "-cp", cp, "com.xdevplatform.xdk.canary.XdkCanaryApp", "--once"]
        if live:
            cmd.append("--live")
        tasks["java"] = cmd

    if "csharp" in sdks:
        dll = build_csharp_examples(csharp_dir, dotnet_bin, env)
        cmd = [dotnet_bin, str(dll), "--canary", "--once"]
        if live:
            cmd.append("--live")
        tasks["csharp"] = cmd

    snapshots: Dict[str, Any] = {}
    overall_ok = True

    def execute_sdk(sdk_name: str, cmd: List[str]) -> Dict[str, Any]:
        cwd = str(java_dir if sdk_name == "java" else csharp_dir)
        proc = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
        snap = parse_last_json_line(proc.stdout)
        snap["exitCode"] = proc.returncode
        return snap

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, len(tasks))) as pool:
        futs = {pool.submit(execute_sdk, name, cmd): name for name, cmd in tasks.items()}
        for fut in concurrent.futures.as_completed(futs):
            name = futs[fut]
            try:
                snap = fut.result()
                snapshots[name] = snap
                if not snap.get("healthy") or snap.get("exitCode", 1) != 0:
                    overall_ok = False
            except Exception as exc:
                overall_ok = False
                snapshots[name] = {"sdk": name, "healthy": False, "error": str(exc)}

    summary = {
        "fleetHealthy": overall_ok,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sdks": snapshots,
    }
    print(json.dumps(summary, indent=2))
    return 0 if overall_ok else 1


class ManagedDaemon:
    def __init__(self, name: str, cmd: List[str], cwd: Path, port: int, env: Dict[str, str]) -> None:
        self.name = name
        self.cmd = cmd
        self.cwd = cwd
        self.port = port
        self.env = env
        self.proc: Optional[subprocess.Popen[str]] = None
        self.restarts = 0
        self.last_line: Optional[str] = None
        self._lock = threading.Lock()

    def start(self) -> None:
        proc = subprocess.Popen(
            self.cmd,
            cwd=str(self.cwd),
            env=self.env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        with self._lock:
            self.proc = proc
        t = threading.Thread(target=self._PumpLogs, args=(proc,), daemon=True)
        t.start()

    def _PumpLogs(self, proc: subprocess.Popen[str]) -> None:
        assert proc.stdout is not None
        for line in proc.stdout:
            stripped = line.strip()
            if stripped:
                with self._lock:
                    self.last_line = stripped
                print(f"[{self.name}] {stripped}", flush=True)

    def ensure_alive(self) -> None:
        with self._lock:
            p = self.proc
        if p is None or p.poll() is not None:
            self.restarts += 1
            print(f"[supervisor] Restarting {self.name} canary daemon (restart #{self.restarts})", flush=True)
            self.start()

    def stop(self) -> None:
        with self._lock:
            p = self.proc
        if p and p.poll() is None:
            p.terminate()
            try:
                p.wait(timeout=5)
            except subprocess.TimeoutExpired:
                p.kill()

    def fetch_json(self, path: str) -> Dict[str, Any]:
        url = f"http://127.0.0.1:{self.port}{path}"
        try:
            with urllib.request.urlopen(url, timeout=3.0) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", errors="replace")
            try:
                return json.loads(raw)
            except Exception:
                return {"sdk": self.name, "healthy": False, "httpStatus": e.code, "error": raw}
        except Exception as exc:
            return {"sdk": self.name, "healthy": False, "error": str(exc)}

    def fetch_metrics(self) -> str:
        url = f"http://127.0.0.1:{self.port}/metrics"
        try:
            with urllib.request.urlopen(url, timeout=3.0) as resp:
                return resp.read().decode("utf-8")
        except Exception:
            return f'xdk_canary_healthy{{sdk="{self.name}"}} 0\n'


def run_daemon_mode(
    sdks: List[str],
    java_dir: Path,
    csharp_dir: Path,
    java_bin: str,
    mvn_bin: str,
    dotnet_bin: str,
    interval_seconds: int,
    supervisor_port: int,
    java_port: int,
    csharp_port: int,
    live: bool,
    env: Dict[str, str],
) -> int:
    daemons: List[ManagedDaemon] = []
    started_at = time.time()

    if "java" in sdks:
        cp = build_java_classpath(java_dir, mvn_bin, env)
        cmd = [
            java_bin,
            "-cp",
            cp,
            "com.xdevplatform.xdk.canary.XdkCanaryApp",
            "--daemon",
            "--interval-seconds",
            str(interval_seconds),
            "--port",
            str(java_port),
        ]
        if live:
            cmd.append("--live")
        daemons.append(ManagedDaemon("java", cmd, java_dir, java_port, env))

    if "csharp" in sdks:
        dll = build_csharp_examples(csharp_dir, dotnet_bin, env)
        cmd = [
            dotnet_bin,
            str(dll),
            "--canary",
            "--daemon",
            "--interval-seconds",
            str(interval_seconds),
            "--port",
            str(csharp_port),
        ]
        if live:
            cmd.append("--live")
        daemons.append(ManagedDaemon("csharp", cmd, csharp_dir, csharp_port, env))

    for d in daemons:
        d.start()

    stop_event = threading.Event()

    class SupervisorHandler(http.server.BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: Any) -> None:
            return

        def do_GET(self) -> None:
            if self.path.startswith("/metrics"):
                lines = [
                    "# TYPE xdk_supervisor_restarts_total counter",
                ]
                fleet_ok = True
                for d in daemons:
                    lines.append(f'xdk_supervisor_restarts_total{{sdk="{d.name}"}} {d.restarts}')
                    st = d.fetch_json("/health")
                    if not st.get("healthy"):
                        fleet_ok = False
                    lines.append(d.fetch_metrics().rstrip("\n"))
                lines.append("# TYPE xdk_supervisor_fleet_healthy gauge")
                lines.append(f"xdk_supervisor_fleet_healthy {1 if fleet_ok else 0}")
                payload = ("\n".join(lines) + "\n").encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
                return

            endpoint = "/status" if self.path.startswith("/status") else "/health"
            sdk_reports: Dict[str, Any] = {}
            fleet_ok = True
            for d in daemons:
                rep = d.fetch_json(endpoint)
                rep["pid"] = d.proc.pid if d.proc else None
                rep["restarts"] = d.restarts
                sdk_reports[d.name] = rep
                latest_ok = rep.get("healthy") if endpoint == "/health" else (rep.get("latest") or {}).get("healthy", False)
                if not latest_ok:
                    fleet_ok = False

            doc = {
                "fleetHealthy": fleet_ok,
                "uptimeSeconds": int(time.time() - started_at),
                "sdks": sdk_reports,
            }
            payload = json.dumps(doc, indent=2).encode("utf-8")
            self.send_response(200 if fleet_ok else 503)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", supervisor_port), SupervisorHandler)
    actual_port = httpd.server_address[1]
    srv_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    srv_thread.start()
    print(
        json.dumps(
            {
                "event": "supervisor_started",
                "url": f"http://127.0.0.1:{actual_port}",
                "sdks": [d.name for d in daemons],
            }
        ),
        flush=True,
    )

    def handle_sig(_signum: int, _frame: Any) -> None:
        stop_event.set()

    signal.signal(signal.SIGINT, handle_sig)
    signal.signal(signal.SIGTERM, handle_sig)

    try:
        while not stop_event.wait(timeout=2.0):
            for d in daemons:
                d.ensure_alive()
    finally:
        httpd.shutdown()
        for d in daemons:
            d.stop()
    return 0


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    workspace_root = repo_root.parent

    parser = argparse.ArgumentParser(description="XDK Multi-SDK Continuous Canary Supervisor")
    parser.add_argument("--sdks", default="java,csharp", help="Comma-separated SDKs to run (default: java,csharp)")
    parser.add_argument("--java-dir", default=str(workspace_root / "xdk-java"))
    parser.add_argument("--csharp-dir", default=str(workspace_root / "xdk-csharp"))
    parser.add_argument("--once", action="store_true", help="Run one verification pass across all selected SDKs and exit")
    parser.add_argument("--daemon", action="store_true", help="Run continuously with aggregated HTTP /health, /status, /metrics")
    parser.add_argument("--interval-seconds", type=int, default=30)
    parser.add_argument("--port", type=int, default=8780, help="Aggregated HTTP supervisor port in --daemon mode")
    parser.add_argument("--java-port", type=int, default=8790)
    parser.add_argument("--csharp-port", type=int, default=8791)
    parser.add_argument("--live", action="store_true", help="Enable live X API probes alongside synthetic simulator probes")
    args = parser.parse_args()

    sdks = [s.strip().lower() for s in args.sdks.split(",") if s.strip()]
    env = os.environ.copy()
    home = Path.home()

    java_home = env.get("JAVA_HOME", "")
    java_fallbacks = [os.path.join(java_home, "bin", "java")] if java_home else []
    java_fallbacks.extend(
        [
            "/opt/homebrew/opt/openjdk/bin/java",
            "/usr/local/opt/openjdk/bin/java",
            "/usr/bin/java",
        ]
    )
    java_bin = env.get("JAVA_BIN") or find_executable("java", java_fallbacks)
    mvn_bin = (
        env.get("MVN_BIN")
        or find_executable("mvn", ["/opt/homebrew/bin/mvn", "/usr/local/bin/mvn", "/usr/bin/mvn"])
        if "java" in sdks
        else ""
    )
    dotnet_bin = (
        env.get("DOTNET_BIN")
        or find_executable(
            "dotnet",
            [
                str(home / ".dotnet" / "dotnet"),
                "/usr/local/share/dotnet/dotnet",
                "/opt/homebrew/bin/dotnet",
                "/usr/bin/dotnet",
            ],
        )
        if "csharp" in sdks
        else ""
    )

    if args.daemon and not args.once:
        return run_daemon_mode(
            sdks=sdks,
            java_dir=Path(args.java_dir),
            csharp_dir=Path(args.csharp_dir),
            java_bin=java_bin,
            mvn_bin=mvn_bin,
            dotnet_bin=dotnet_bin,
            interval_seconds=args.interval_seconds,
            supervisor_port=args.port,
            java_port=args.java_port,
            csharp_port=args.csharp_port,
            live=args.live,
            env=env,
        )

    return run_once_mode(
        sdks=sdks,
        java_dir=Path(args.java_dir),
        csharp_dir=Path(args.csharp_dir),
        java_bin=java_bin,
        mvn_bin=mvn_bin,
        dotnet_bin=dotnet_bin,
        live=args.live,
        env=env,
    )


if __name__ == "__main__":
    sys.exit(main())
