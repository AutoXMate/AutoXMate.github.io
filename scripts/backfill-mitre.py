#!/usr/bin/env python3
"""
Backfill MITRE ATT&CK IDs for security/recon/exploitation tools based on their domain.
"""

import sys
import re
import yaml
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "tools"

# MITRE mappings by namespace pattern
MITRE_MAP = [
    # Reconnaissance
    (["security:recon", "security:discovery", "security:osint", "network:scan"], 
     ["T1595", "T1046"]),
    # Enumeration 
    (["security:enumeration", "network:dns", "network:snmp", "network:ldap"],
     ["T1046", "T1592", "T1069"]),
    # Credential access
    (["security:credential", "security:password", "security:crack", "security:hashcat",
      "security:hash", "security:kerberos", "security:ntlm", "security:adcs"],
     ["T1555", "T1558", "T1110"]),
    # Exploitation
    (["security:exploit", "security:payload", "security:shell", "security:backdoor",
      "security:webshell", "security:dropper"],
     ["T1203", "T1059", "T1190"]),
    # Persistence
    (["security:persistence", "windows:persistence", "windows:boot", "windows:service"],
     ["T1543", "T1547", "T1053"]),
    # Privilege escalation
    (["security:privesc", "windows:privesc", "windows:bypass", "security:bypass",
      "security:sudo", "security:suid"],
     ["T1548", "T1068", "T1055"]),
    # Defense evasion
    (["security:evasion", "windows:evasion", "security:obfuscation", "security:bypass-uac",
      "windows:amsi"],
     ["T1562", "T1055", "T1027", "T1564"]),
    # Lateral movement
    (["security:lateral", "windows:lateral", "network:smb", "network:winrm",
      "windows:psremoting", "windows:psexec", "windows:wmi"],
     ["T1021", "T1570", "T1550"]),
    # Collection / exfiltration
    (["security:collection", "security:exfil", "windows:clipboard", "network:ftp",
      "network:http"],
     ["T1005", "T1048", "T1074", "T1114"]),
    # Command and control
    (["security:c2", "security:command", "security:dns-tunnel", "network:proxy",
      "network:reverse"],
     ["T1071", "T1573", "T1090", "T1572"]),
    # Discovery
    (["windows:discovery", "system:discovery", "network:discovery"],
     ["T1082", "T1087", "T1046", "T1012"]),
    # Impact
    (["security:impact", "security:ransomware", "security:destruction"],
     ["T1486", "T1485", "T1499"]),
    # Execution  
    (["windows:execution", "windows:run", "windows:script", "windows:mshta",
      "windows:rundll32", "windows:regsvr32", "windows:cscript", "windows:wscript",
      "windows:msbuild", "windows:installutil", "windows:reg"],
     ["T1204", "T1059", "T1218", "T1129"]),
    # System tools
    (["system:terminal", "system:shell", "system:process"],
     ["T1059"]),
    # Web application
    (["web:scan", "web:exploit", "web:attack", "security:web", "network:http"],
     ["T1190", "T1595", "T1046"]),
    # Archive
    (["archive", "compression"],
     ["T1560"]),
]

# Tool-specific MITRE overrides (name -> mitre_ids)
TOOL_MITRE = {
    "nmap": ["T1046", "T1595"],
    "masscan": ["T1046", "T1595"],
    "hydra": ["T1110"],
    "hashcat": ["T1110"],
    "john": ["T1110"],
    "sqlmap": ["T1190"],
    "metasploit": ["T1203", "T1059", "T1190"],
    "crackmapexec": ["T1021", "T1110"],
    "responder": ["T1557", "T1046"],
    "bloodhound": ["T1087", "T1069"],
    "mimikatz": ["T1555", "T1003", "T1055"],
    "gobuster": ["T1595", "T1046"],
    "ffuf": ["T1595"],
    "dirb": ["T1595"],
    "nikto": ["T1595", "T1046"],
    "nuclei": ["T1595"],
    "subfinder": ["T1595"],
    "amass": ["T1595"],
    "dnscan": ["T1595"],
    "theharvester": ["T1595"],
    "dnsrecon": ["T1595"],
    "wpscan": ["T1595", "T1190"],
    "smbmap": ["T1021", "T1046"],
    "enum4linux": ["T1046", "T1069"],
    "ldapsearch": ["T1087", "T1069"],
    "impacket": ["T1021", "T1558", "T1550"],
    "certipy": ["T1558", "T1649"],
    "evil-winrm": ["T1021"],
    "psexec": ["T1021", "T1569"],
    "wmiexec": ["T1021", "T1047"],
    "wmicexec": ["T1021", "T1047"],
    "powershell": ["T1059", "T1086"],
    "cobaltstrike": ["T1071", "T1573", "T1059"],
    "sliver": ["T1071", "T1573", "T1059"],
    "havoc": ["T1071", "T1573"],
    "bruterr": ["T1110"],
    "medusa": ["T1110"],
    "ncrack": ["T1110"],
    "johnny": ["T1110"],
    "keepass": ["T1555"],
    "laZagne": ["T1555"],
    "seclists": ["T1595"],
    "payloadsallthethings": ["T1595"],
    "payloadbox": ["T1595"],
}


def load_tool(filename):
    fpath = TOOLS_DIR / filename
    if not fpath.exists():
        return None, None
    content = fpath.read_text(encoding="utf-8", errors="replace")
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)', content, re.DOTALL)
    if not fm_match:
        return None, content
    try:
        data = yaml.safe_load(fm_match.group(1))
    except yaml.YAMLError:
        return None, content
    return data if isinstance(data, dict) else None, fm_match.group(2)


def dump_frontmatter(data):
    return yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True).strip()


def infer_mitre(data, filename):
    """Infer MITRE ATT&CK IDs from namespace and name."""
    namespace = data.get("namespace", "").lower()
    name = data.get("name", "").lower()
    tool_name = filename.replace(".md", "")
    
    # Check tool-specific mapping first
    if tool_name in TOOL_MITRE:
        return list(TOOL_MITRE[tool_name])
    if name in TOOL_MITRE:
        return list(TOOL_MITRE[name])
    
    # Check namespace prefix-based mapping
    matched = set()
    for patterns, mitre_ids in MITRE_MAP:
        for pat in patterns:
            if pat in namespace:
                matched.update(mitre_ids)
                break
    
    return sorted(matched) if matched else None


def main():
    dry_run = "--dry-run" in sys.argv
    dry_run = False if "--apply" in sys.argv else dry_run
    
    md_files = sorted(TOOLS_DIR.glob("*.md"))
    total = len(md_files)
    changed = 0
    
    if dry_run:
        print(f"AutoXMate MITRE Backfill (DRY RUN)")
    else:
        print(f"AutoXMate MITRE Backfill (APPLYING)")
    
    for fpath in md_files:
        filename = fpath.name
        if filename in ("index.md",):
            continue
        
        data, body = load_tool(filename)
        if data is None:
            continue
        
        # Skip tools that already have MITRE IDs
        if data.get("mitre_ids"):
            continue
        
        mitre_ids = infer_mitre(data, filename)
        if not mitre_ids:
            continue
        
        if dry_run:
            print(f"  [{filename}] +mitre_ids: {mitre_ids}")
            changed += 1
            continue
        
        data["mitre_ids"] = mitre_ids
        new_fm = dump_frontmatter(data)
        new_content = f"---\n{new_fm}\n---\n\n{body.strip()}\n"
        fpath.write_text(new_content, encoding="utf-8")
        changed += 1
    
    print(f"\nSummary: {changed} tools updated (out of {total})")
    if dry_run:
        print("Run with --apply to write changes")


if __name__ == "__main__":
    main()
