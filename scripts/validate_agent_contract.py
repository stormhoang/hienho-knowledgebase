#!/usr/bin/env python3
"""Validate the Agent-facing operating contracts and capability registry."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "AGENT_OPERATING_CONTRACT.md",
    ROOT / "00_HARNESS_CORE" / "AGENT_CAPABILITIES.yaml",
    ROOT / "00_HARNESS_CORE" / "AGENT_SAFETY_CONTRACT.yaml",
    ROOT / "00_HARNESS_CORE" / "AGENT_OUTPUT_CONTRACT.md",
]
REQUIRED_CAPABILITY_KEYS = {"purpose", "entrypoint", "read_only", "requires_approval", "external_write"}


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        print("Missing contract files:", ", ".join(missing))
        return 1

    try:
        import yaml
    except ImportError:
        print("PyYAML is required to validate AGENT_CAPABILITIES.yaml")
        return 1

    registry = yaml.safe_load((ROOT / "00_HARNESS_CORE" / "AGENT_CAPABILITIES.yaml").read_text())
    capabilities = registry.get("capabilities", {})
    errors = []
    for name, capability in capabilities.items():
        missing_keys = REQUIRED_CAPABILITY_KEYS - capability.keys()
        if missing_keys:
            errors.append(f"{name}: thiếu {', '.join(sorted(missing_keys))}")
        entrypoint = ROOT / capability.get("entrypoint", "")
        if not entrypoint.exists():
            errors.append(f"{name}: không tìm thấy entrypoint {capability.get('entrypoint')}")
        if capability.get("requires_approval") and capability.get("read_only"):
            errors.append(f"{name}: read_only không thể đồng thời yêu cầu approval")
        if capability.get("external_write") and capability.get("read_only"):
            errors.append(f"{name}: external_write không thể đồng thời read_only")

    if errors:
        print("Agent contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Agent contract valid: {len(capabilities)} capabilities")
    return 0


if __name__ == "__main__":
    sys.exit(main())
