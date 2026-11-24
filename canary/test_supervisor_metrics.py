"""Unit tests for Prometheus exposition aggregation in canary/supervisor.py."""

from __future__ import annotations

from supervisor import aggregate_prometheus_metrics


def test_aggregate_prometheus_metrics_deduplicates_type_lines_and_groups_families() -> None:
    python_metrics = "\n".join(
        [
            "# TYPE xdk_canary_cycles_total counter",
            'xdk_canary_cycles_total{sdk="python"} 4',
            "# TYPE xdk_canary_probe_failures_total counter",
            'xdk_canary_probe_failures_total{sdk="python"} 0',
            "# TYPE xdk_canary_healthy gauge",
            'xdk_canary_healthy{sdk="python"} 1',
            "# TYPE xdk_canary_probe_duration_ms gauge",
            'xdk_canary_probe_duration_ms{sdk="python",probe="posts",mode="mock"} 12',
            "# TYPE xdk_canary_probe_success gauge",
            'xdk_canary_probe_success{sdk="python",probe="posts",mode="mock"} 1',
        ]
    )
    ts_metrics = "\n".join(
        [
            "# TYPE xdk_canary_cycles_total counter",
            'xdk_canary_cycles_total{sdk="typescript"} 4',
            "# TYPE xdk_canary_probe_failures_total counter",
            'xdk_canary_probe_failures_total{sdk="typescript"} 0',
            "# TYPE xdk_canary_healthy gauge",
            'xdk_canary_healthy{sdk="typescript"} 1',
            "# TYPE xdk_canary_probe_duration_ms gauge",
            'xdk_canary_probe_duration_ms{sdk="typescript",probe="posts",mode="mock"} 8',
            "# TYPE xdk_canary_probe_success gauge",
            'xdk_canary_probe_success{sdk="typescript",probe="posts",mode="mock"} 1',
        ]
    )
    # Down daemon fallback emits a bare sample line without `# TYPE`
    down_java_metrics = 'xdk_canary_healthy{sdk="java"} 0\n'

    merged = aggregate_prometheus_metrics(
        [
            ("python", 0, python_metrics),
            ("typescript", 1, ts_metrics),
            ("java", 2, down_java_metrics),
        ],
        fleet_ok=False,
    )

    lines = [ln for ln in merged.splitlines() if ln.strip()]
    type_lines = [ln for ln in lines if ln.startswith("# TYPE ")]
    assert len(type_lines) == len(set(type_lines)), f"Duplicate # TYPE lines in:\n{merged}"

    expected_types = {
        "# TYPE xdk_supervisor_restarts_total counter",
        "# TYPE xdk_canary_cycles_total counter",
        "# TYPE xdk_canary_probe_failures_total counter",
        "# TYPE xdk_canary_healthy gauge",
        "# TYPE xdk_canary_probe_duration_ms gauge",
        "# TYPE xdk_canary_probe_success gauge",
        "# TYPE xdk_supervisor_fleet_healthy gauge",
    }
    assert set(type_lines) == expected_types

    # Verify samples are strictly grouped by metric family (never interleaved)
    seen_families: list[str] = []
    for ln in lines:
        if ln.startswith("#"):
            continue
        fam = ln.split("{", 1)[0].split(None, 1)[0]
        if not seen_families or seen_families[-1] != fam:
            assert fam not in seen_families, f"Metric family {fam} interleaved in:\n{merged}"
            seen_families.append(fam)

    assert 'xdk_canary_healthy{sdk="java"} 0' in merged
    assert "xdk_supervisor_fleet_healthy 0" in merged
