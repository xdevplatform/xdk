#!/usr/bin/env python3
"""
Unified 4-SDK Continuous Canary Supervisor for XDK.

Runs and supervises the Python (`xdk-python`), TypeScript (`xdk-typescript`),
Java (`xdk-java`), and C# (`xdk-csharp`) continuous SDK canary environments
either as a single verification pass (`--once`) or as an always-on background service (`--daemon`)
exposing aggregated `/health`, `/status`, and Prometheus `/metrics` endpoints.

Usage:
  # Run one full 4-SDK canary verification pass:
  python3 canary/supervisor.py --once --live

  # Run continuously as an always-on 4-SDK fleet canary daemon on port 8780:
  python3 canary/supervisor.py --daemon --live --interval-seconds 30 --port 8780
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
from typing import Any, Dict, List, Optional, Tuple


def find_executable(name: str, fallbacks: List[str]) -> str:
    found = shutil.which(name)
    if found:
        return found
    for candidate in fallbacks:
        if candidate and os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    raise FileNotFoundError(f"Could not find `{name}` on PATH or in {fallbacks}")


def prepare_python_canary(python_dir: Path, uv_bin: str, env: Dict[str, str]) -> str:
    venv_python = python_dir / ".venv" / "bin" / "python"
    if not venv_python.is_file():
        subprocess.run(
            [uv_bin, "sync"],
            cwd=str(python_dir),
            env=env,
            stdout=sys.stderr,
            check=True,
        )
    if not venv_python.is_file():
        raise FileNotFoundError(f"Expected Python virtualenv interpreter at {venv_python}")
    return str(venv_python)


def prepare_typescript_canary(
    typescript_dir: Path, node_bin: str, npm_bin: str, env: Dict[str, str]
) -> Path:
    tsup_bin = typescript_dir / "node_modules" / ".bin" / "tsup"
    if not tsup_bin.is_file():
        subprocess.run(
            [npm_bin, "install", "--no-audit", "--no-fund"],
            cwd=str(typescript_dir),
            env=env,
            stdout=sys.stderr,
            check=True,
        )
    subprocess.run(
        [
            str(tsup_bin),
            "examples/canary.ts",
            "--no-config",
            "--no-dts",
            "--format",
            "esm",
            "--out-dir",
            ".xdk-examples",
            "--silent",
        ],
        cwd=str(typescript_dir),
        env=env,
        stdout=sys.stderr,
        check=True,
    )
    bundle = typescript_dir / ".xdk-examples" / "canary.js"
    if not bundle.is_file():
        raise FileNotFoundError(f"Expected bundled TypeScript canary at {bundle}")
    return bundle


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
        stdout=sys.stderr,
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
        stdout=sys.stderr,
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


def build_sdk_commands(
    sdks: List[str],
    dirs: Dict[str, Path],
    bins: Dict[str, str],
    mode: str,
    interval_seconds: int,
    ports: Dict[str, int],
    live: bool,
    env: Dict[str, str],
) -> Dict[str, Tuple[List[str], Path, int]]:
    specs: Dict[str, Tuple[List[str], Path, int]] = {}

    if "python" in sdks:
        py_exe = prepare_python_canary(dirs["python"], bins["uv"], env)
        cmd = [py_exe, "-m", "examples.canary"]
        if mode == "once":
            cmd.append("--once")
        else:
            cmd.extend(["--daemon", "--interval-seconds", str(interval_seconds), "--port", str(ports["python"])])
        if live:
            cmd.append("--live")
        specs["python"] = (cmd, dirs["python"], ports["python"])

    if "typescript" in sdks:
        bundle = prepare_typescript_canary(dirs["typescript"], bins["node"], bins["npm"], env)
        cmd = [bins["node"], str(bundle)]
        if mode == "once":
            cmd.append("--once")
        else:
            cmd.extend(["--daemon", "--interval-seconds", str(interval_seconds), "--port", str(ports["typescript"])])
        if live:
            cmd.append("--live")
        specs["typescript"] = (cmd, dirs["typescript"], ports["typescript"])

    if "java" in sdks:
        cp = build_java_classpath(dirs["java"], bins["mvn"], env)
        cmd = [bins["java"], "-cp", cp, "com.xdevplatform.xdk.canary.XdkCanaryApp"]
        if mode == "once":
            cmd.append("--once")
        else:
            cmd.extend(["--daemon", "--interval-seconds", str(interval_seconds), "--port", str(ports["java"])])
        if live:
            cmd.append("--live")
        specs["java"] = (cmd, dirs["java"], ports["java"])

    if "csharp" in sdks:
        dll = build_csharp_examples(dirs["csharp"], bins["dotnet"], env)
        cmd = [bins["dotnet"], str(dll), "--canary"]
        if mode == "once":
            cmd.append("--once")
        else:
            cmd.extend(["--daemon", "--interval-seconds", str(interval_seconds), "--port", str(ports["csharp"])])
        if live:
            cmd.append("--live")
        specs["csharp"] = (cmd, dirs["csharp"], ports["csharp"])

    return specs


def run_once_mode(
    sdks: List[str],
    dirs: Dict[str, Path],
    bins: Dict[str, str],
    ports: Dict[str, int],
    live: bool,
    env: Dict[str, str],
) -> int:
    specs = build_sdk_commands(sdks, dirs, bins, "once", 60, ports, live, env)
    snapshots: Dict[str, Any] = {}
    overall_ok = True

    def execute_sdk(sdk_name: str, cmd: List[str], cwd: Path) -> Dict[str, Any]:
        proc = subprocess.run(cmd, cwd=str(cwd), env=env, capture_output=True, text=True)
        if proc.returncode != 0 and not proc.stdout.strip():
            raise RuntimeError(f"{sdk_name} exited {proc.returncode}: {proc.stderr}")
        snap = parse_last_json_line(proc.stdout)
        snap["exitCode"] = proc.returncode
        return snap

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, len(specs))) as pool:
        futs = {
            pool.submit(execute_sdk, name, cmd, cwd): name
            for name, (cmd, cwd, _port) in specs.items()
        }
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

    ordered = {name: snapshots[name] for name in sdks if name in snapshots}
    summary = {
        "fleetHealthy": overall_ok,
        "sdkCount": len(ordered),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sdks": ordered,
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
        t = threading.Thread(target=self._pump_logs, args=(proc,), daemon=True)
        t.start()

    def _pump_logs(self, proc: subprocess.Popen[str]) -> None:
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
    dirs: Dict[str, Path],
    bins: Dict[str, str],
    interval_seconds: int,
    supervisor_port: int,
    ports: Dict[str, int],
    live: bool,
    env: Dict[str, str],
) -> int:
    specs = build_sdk_commands(sdks, dirs, bins, "daemon", interval_seconds, ports, live, env)
    daemons: List[ManagedDaemon] = [
        ManagedDaemon(name, cmd, cwd, port, env)
        for name, (cmd, cwd, port) in specs.items()
    ]
    started_at = time.time()

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
                latest_ok = (
                    rep.get("healthy")
                    if endpoint == "/health"
                    else (rep.get("latest") or {}).get("healthy", False)
                )
                if not latest_ok:
                    fleet_ok = False

            doc = {
                "fleetHealthy": fleet_ok,
                "sdkCount": len(daemons),
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

    parser = argparse.ArgumentParser(description="XDK 4-SDK Continuous Canary Supervisor")
    parser.add_argument(
        "--sdks",
        default="python,typescript,java,csharp",
        help="Comma-separated SDKs to run (default: python,typescript,java,csharp)",
    )
    parser.add_argument("--python-dir", default=str(workspace_root / "xdk-python"))
    parser.add_argument("--typescript-dir", default=str(workspace_root / "xdk-typescript"))
    parser.add_argument("--java-dir", default=str(workspace_root / "xdk-java"))
    parser.add_argument("--csharp-dir", default=str(workspace_root / "xdk-csharp"))
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run one verification pass across all selected SDKs and exit",
    )
    parser.add_argument(
        "--daemon",
        action="store_true",
        help="Run continuously with aggregated HTTP /health, /status, /metrics",
    )
    parser.add_argument("--interval-seconds", type=int, default=30)
    parser.add_argument(
        "--port",
        type=int,
        default=8780,
        help="Aggregated HTTP supervisor port in --daemon mode",
    )
    parser.add_argument("--java-port", type=int, default=8790)
    parser.add_argument("--csharp-port", type=int, default=8791)
    parser.add_argument("--python-port", type=int, default=8792)
    parser.add_argument("--typescript-port", type=int, default=8793)
    parser.add_argument(
        "--live",
        action="store_true",
        help="Enable live X API probes alongside synthetic simulator probes",
    )
    args = parser.parse_args()

    sdks = [s.strip().lower() for s in args.sdks.split(",") if s.strip()]
    env = os.environ.copy()
    home = Path.home()

    bins: Dict[str, str] = {}
    if "python" in sdks:
        venv_py = Path(args.python_dir) / ".venv" / "bin" / "python"
        bins["uv"] = (
            env.get("UV_BIN")
            or (
                ""
                if venv_py.is_file()
                else find_executable(
                    "uv",
                    [
                        str(home / ".local" / "bin" / "uv"),
                        str(home / ".cargo" / "bin" / "uv"),
                        "/opt/homebrew/bin/uv",
                        "/usr/local/bin/uv",
                    ],
                )
            )
        )

    if "typescript" in sdks:
        bins["node"] = env.get("NODE_BIN") or find_executable(
            "node",
            [
                str(home / ".local" / "bin" / "node"),
                "/opt/homebrew/bin/node",
                "/usr/local/bin/node",
                "/usr/bin/node",
            ],
        )
        node_dir = str(Path(bins["node"]).parent)
        env["PATH"] = f"{node_dir}{os.pathsep}{env.get('PATH', '')}"
        bins["npm"] = env.get("NPM_BIN") or find_executable(
            "npm",
            [
                str(Path(node_dir) / "npm"),
                "/opt/homebrew/bin/npm",
                "/usr/local/bin/npm",
                "/usr/bin/npm",
            ],
        )

    if "java" in sdks:
        java_home = env.get("JAVA_HOME", "")
        java_fallbacks = [os.path.join(java_home, "bin", "java")] if java_home else []
        java_fallbacks.extend(
            [
                "/opt/homebrew/opt/openjdk/bin/java",
                "/usr/local/opt/openjdk/bin/java",
                "/usr/bin/java",
            ]
        )
        bins["java"] = env.get("JAVA_BIN") or find_executable("java", java_fallbacks)
        bins["mvn"] = env.get("MVN_BIN") or find_executable(
            "mvn", ["/opt/homebrew/bin/mvn", "/usr/local/bin/mvn", "/usr/bin/mvn"]
        )

    if "csharp" in sdks:
        bins["dotnet"] = env.get("DOTNET_BIN") or find_executable(
            "dotnet",
            [
                str(home / ".dotnet" / "dotnet"),
                "/usr/local/share/dotnet/dotnet",
                "/opt/homebrew/bin/dotnet",
                "/usr/bin/dotnet",
            ],
        )

    dirs = {
        "python": Path(args.python_dir),
        "typescript": Path(args.typescript_dir),
        "java": Path(args.java_dir),
        "csharp": Path(args.csharp_dir),
    }
    ports = {
        "java": args.java_port,
        "csharp": args.csharp_port,
        "python": args.python_port,
        "typescript": args.typescript_port,
    }

    if args.daemon and not args.once:
        return run_daemon_mode(
            sdks=sdks,
            dirs=dirs,
            bins=bins,
            interval_seconds=args.interval_seconds,
            supervisor_port=args.port,
            ports=ports,
            live=args.live,
            env=env,
        )

    return run_once_mode(
        sdks=sdks,
        dirs=dirs,
        bins=bins,
        ports=ports,
        live=args.live,
        env=env,
    )


if __name__ == "__main__":
    sys.exit(main())
