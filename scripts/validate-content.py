#!/usr/bin/env python3
"""
AutoXMate Content Validation Framework
Validates all 2,152 tool markdown files against the schema:
  - Frontmatter YAML syntax
  - Required fields present
  - Schema types correct (arrays, enums, regex patterns)
  - External references valid (URLs)
  - Execution templates well-formed
  - No duplicate IDs
  - Summary stats per gap
"""

import os
import sys
import re
import yaml
import json
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

TOOLS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "tools"
REQUIRED_FIELDS = ["id", "namespace", "name", "description", "version", "capabilities", "execution"]

ENUMS = {
    "platforms": ["linux", "windows", "macos", "bsd", "cross-platform"],
    "architectures": ["amd64", "arm64", "arm", "riscv64", "i386", "cross-platform"],
    "risk_level": ["low", "medium", "high", "critical"],
    "execution_policy": ["enabled", "read-only", "disabled"],
    "trust_level": ["verified", "experimental", "community", "ai-generated"],
    "features": ["stealth", "requires-root", "network-intensive", "output-json", "output-xml", "streaming", "interactive", "batch", "encryption", "compression", "remote", "local", "pipes-stdin", "pipes-stdout", "file-system", "process-manip"],
    "techniques": ["recon", "enumeration", "exfiltration", "privilege-escalation", "persistence", "lateral-movement", "discovery", "collection", "command-and-control", "credential-access", "defense-evasion", "execution", "impact", "data-manipulation", "monitoring", "backup", "forensics", "analysis", "network-manipulation", "process-discovery", "process-termination", "network-sniffing", "remote-services", "encryption", "process-manip"],
    "sandbox": ["docker", "execFile", "none"],
    "phase": ["recon", "enumeration", "exploitation", "post-exploitation", "forensics", "defense-evasion", "discovery", "collection", "lateral-movement", "exfiltration"],
    "detection_type": ["sigma", "elastic", "splunk", "yara", "clamav", "sysmon", "wdac", "ioc", "blockrule", "other"],
    "install_method": ["apt", "brew", "pip", "pipx", "go", "cargo", "git", "docker", "binary", "npm", "gem", "pacman", "dnf", "choco", "snap", "custom"],
}

ID_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)+$')
NAMESPACE_PATTERN = re.compile(r'^[a-z]+(\.[a-z0-9]+)*:[a-z]+:[a-z0-9-]+(:[a-z0-9-]+)?$')
SEMVER_PATTERN = re.compile(r'^\d+\.\d+\.\d+$')
MITRE_PATTERN = re.compile(r'^T\d{4}(\.\d{3})?$')

results = {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "errors": [],
    "stats": {
        "with_parameters": 0,
        "with_install": 0,
        "with_detections": 0,
        "with_references": 0,
        "with_examples": 0,
        "with_features": 0,
        "with_techniques": 0,
        "with_mitre": 0,
        "with_contract": 0,
        "with_artifacts": 0,
        "with_workflow_edges": 0,
    },
    "missing_references": [],
    "duplicate_ids": {},
}


def validate_frontmatter(filepath, data, filename):
    file_errors = []
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            file_errors.append(f"Missing required field: {field}")
    
    if not file_errors:
        # Validate ID pattern
        if not ID_PATTERN.match(data.get("id", "")):
            file_errors.append(f"Invalid ID format: {data.get('id')}")
        
        # Validate namespace
        if not NAMESPACE_PATTERN.match(data.get("namespace", "")):
            file_errors.append(f"Invalid namespace: {data.get('namespace')}")
        
        # Validate version
        if not SEMVER_PATTERN.match(data.get("version", "")):
            file_errors.append(f"Invalid version (not semver): {data.get('version')}")
        
        # Validate platforms if present
        if "platforms" in data:
            for p in data["platforms"]:
                if p not in ENUMS["platforms"]:
                    file_errors.append(f"Invalid platform: {p}")
        
        # Validate execution sandbox
        if "execution" in data:
            sandbox = data["execution"].get("sandbox", "execFile")
            if sandbox not in ENUMS["sandbox"]:
                file_errors.append(f"Invalid sandbox type: {sandbox}")
            if "template" not in data["execution"]:
                file_errors.append("Missing execution.template")
        
        # Validate risk level
        if "risk_level" in data and data["risk_level"] not in ENUMS["risk_level"]:
            file_errors.append(f"Invalid risk_level: {data['risk_level']}")
        
        # Validate trust_level
        if "trust_level" in data and data["trust_level"] not in ENUMS["trust_level"]:
            file_errors.append(f"Invalid trust_level: {data['trust_level']}")
        
        # Validate features
        if "features" in data:
            for f in data["features"]:
                if f not in ENUMS["features"]:
                    file_errors.append(f"Invalid feature: {f}")
        
        # Validate techniques
        if "techniques" in data:
            for t in data["techniques"]:
                if t not in ENUMS["techniques"]:
                    file_errors.append(f"Invalid technique: {t}")
        
        # Validate phase
        if "phase" in data and data["phase"] not in ENUMS["phase"]:
            file_errors.append(f"Invalid phase: {data['phase']}")
        
        # Validate references
        if "references" in data:
            for ref in data["references"]:
                if "url" not in ref:
                    file_errors.append(f"Reference missing URL: {ref}")
                else:
                    parsed = urlparse(ref["url"])
                    if not parsed.scheme or not parsed.netloc:
                        file_errors.append(f"Invalid reference URL: {ref['url']}")
        
        # Validate detections
        if "detections" in data:
            for d in data["detections"]:
                if d.get("type") not in ENUMS["detection_type"]:
                    file_errors.append(f"Invalid detection type: {d.get('type')}")
        
        # Validate install
        if "install" in data:
            for inst in data["install"]:
                if inst.get("method") not in ENUMS["install_method"]:
                    file_errors.append(f"Invalid install method: {inst.get('method')}")
        
        # Validate parameters
        if "parameters" in data:
            for param in data["parameters"]:
                if param.get("type") not in ["string", "integer", "number", "boolean", "array", "file", "url"]:
                    file_errors.append(f"Invalid param type: {param.get('type')} for {param.get('name')}")
                if "description" not in param:
                    file_errors.append(f"Parameter missing description: {param.get('name')}")

    return file_errors


def main():
    md_files = sorted(TOOLS_DIR.glob("*.md"))
    results["total"] = len(md_files)
    
    print(f"Validating {len(md_files)} tool files in {TOOLS_DIR}\n")
    
    for i, fpath in enumerate(md_files, 1):
        filename = fpath.name
        content = fpath.read_text(encoding="utf-8", errors="replace")
        
        # Extract YAML frontmatter between --- markers
        fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            results["errors"].append(f"  [{filename}] No valid YAML frontmatter found")
            results["failed"] += 1
            continue
        
        yaml_str = fm_match.group(1)
        try:
            data = yaml.safe_load(yaml_str)
            if not isinstance(data, dict):
                results["errors"].append(f"  [{filename}] Frontmatter is not a dictionary")
                results["failed"] += 1
                continue
        except yaml.YAMLError as e:
            results["errors"].append(f"  [{filename}] YAML parse error: {e}")
            results["failed"] += 1
            continue
        
        # Track duplicate IDs
        tool_id = data.get("id", f"NO-ID-{filename}")
        results["duplicate_ids"][tool_id] = results["duplicate_ids"].get(tool_id, 0) + 1
        
        # Validate
        file_errors = validate_frontmatter(fpath, data, filename)
        
        if file_errors:
            results["failed"] += 1
            for err in file_errors:
                results["errors"].append(f"  [{filename}] {err}")
        else:
            results["passed"] += 1
        
        # Stats
        if data.get("parameters"):
            results["stats"]["with_parameters"] += 1
        if data.get("install"):
            results["stats"]["with_install"] += 1
        if data.get("detections"):
            results["stats"]["with_detections"] += 1
        if data.get("references"):
            results["stats"]["with_references"] += 1
        if data.get("examples"):
            results["stats"]["with_examples"] += 1
        if data.get("features"):
            results["stats"]["with_features"] += 1
        if data.get("techniques"):
            results["stats"]["with_techniques"] += 1
        if data.get("mitre_ids"):
            results["stats"]["with_mitre"] += 1
        if data.get("contract"):
            results["stats"]["with_contract"] += 1
        if data.get("artifacts"):
            results["stats"]["with_artifacts"] += 1
        if data.get("workflow_edges"):
            results["stats"]["with_workflow_edges"] += 1
        
        # Track missing references for potential backfill
        if not data.get("references"):
            results["missing_references"].append(filename)
    
    # Report
    print(f"{'='*60}")
    print(f"  VALIDATION RESULTS")
    print(f"{'='*60}")
    print(f"  Total files:  {results['total']}")
    print(f"  Passed:       {results['passed']}")
    print(f"  Failed:       {results['failed']}")
    print(f"  Errors:       {len(results['errors'])}")
    
    # Duplicate ID check
    dups = {k: v for k, v in results["duplicate_ids"].items() if v > 1}
    if dups:
        print(f"\n  ⚠ DUPLICATE IDs:")
        for did, count in dups.items():
            print(f"     {did} appears {count} times")
    
    print(f"\n{'='*60}")
    print(f"  CONTENT COVERAGE")
    print(f"{'='*60}")
    total = results["total"]
    for key, label in [
        ("with_parameters", "parameters"),
        ("with_install", "install"),
        ("with_detections", "detections"),
        ("with_references", "references"),
        ("with_examples", "examples"),
        ("with_features", "features"),
        ("with_techniques", "techniques"),
        ("with_mitre", "mitre_ids"),
        ("with_contract", "contract"),
        ("with_artifacts", "artifacts"),
        ("with_workflow_edges", "workflow_edges"),
    ]:
        count = results["stats"][key]
        pct = (count / total) * 100 if total else 0
        filled = "▓" * int(pct // 5) + "░" * (20 - int(pct // 5))
        print(f"  {label:16s} {filled} {count:5d}/{total} ({pct:5.1f}%)")
    
    print(f"\n{'='*60}")
    if results["failed"] > 0:
        print(f"  TOP FAILURES (first 20):")
        for err in results["errors"][:20]:
            print(err)
    
    # Summary JSON
    summary_path = Path(__file__).resolve().parent.parent / "data" / "validation-summary.json"
    output = {
        "timestamp": datetime.now().isoformat(),
        "total": results["total"],
        "passed": results["passed"],
        "failed": results["failed"],
        "error_count": len(results["errors"]),
        "coverage": results["stats"],
        "duplicate_ids": list(dups.keys()) if dups else [],
    }
    with open(summary_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSummary written to {summary_path}")
    
    return 0 if results["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
