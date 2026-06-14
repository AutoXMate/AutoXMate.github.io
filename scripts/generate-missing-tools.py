#!/usr/bin/env python3
"""
AutoXMate Batch Tool Generator (v2)
Generates new tool entries for missing CLI commands with proper frontmatter.
"""

import sys
import yaml
from pathlib import Path

TOOLS_DIR = Path(__file__).parent.parent / "src" / "content" / "tools"

NEW_TOOLS = [
    # Windows CMD commands
    ("systeminfo", "systeminfo", "system:windows:cmd", "windows",
     "Displays detailed system configuration including OS version, build, and hardware specs.",
     None, ["windows"], []),
    ("hostname", "hostname", "system:windows:cmd", "windows",
     "Displays the host name portion of the full computer name.",
     None, ["windows"], []),
    ("driverquery", "driverquery", "system:windows:driver", "windows",
     "Lists all installed device drivers and their properties.",
     None, ["windows"], []),
    ("set", "set", "system:windows:cmd", "windows",
     "Displays, sets, or removes environment variables.",
     None, ["windows"], []),
    ("nslookup", "nslookup", "network:dns:lookup", "network",
     "Queries DNS servers for domain name or IP resolution.",
     "custom", ["linux","windows"], ["T1590"]),
    ("tasklist", "tasklist", "system:windows:process", "windows",
     "Displays currently running processes with PID, session, and memory usage.",
     None, ["windows"], ["T1057"]),
    ("net", "net", "system:windows:networking", "windows",
     "Network administration command for users, groups, shares, services, and connections.",
     None, ["windows"], []),
    ("where", "where", "system:windows:file", "windows",
     "Displays file locations matching a search pattern.",
     None, ["windows"], []),
    ("dir", "dir", "system:windows:file", "windows",
     "Displays files and subdirectories in a directory.",
     None, ["windows"], []),
    ("wevtutil", "wevtutil", "system:windows:logging", "windows",
     "Retrieves event log information, exports, archives, and clears logs.",
     None, ["windows"], []),
    ("gpresult", "gpresult", "system:windows:policy", "windows",
     "Displays Resultant Set of Policy (RSoP) for a user and computer.",
     None, ["windows"], []),
    ("shutdown", "shutdown", "system:windows:admin", "windows",
     "Shuts down, restarts, or logs off local or remote computers.",
     None, ["windows"], []),
    ("bcdedit", "bcdedit", "system:windows:boot", "windows",
     "Boot Configuration Data editor for managing boot configuration.",
     None, ["windows"], []),
    ("vssadmin", "vssadmin", "system:windows:backup", "windows",
     "Volume Shadow Copy Service administration tool.",
     None, ["windows"], []),
    ("ipconfig", "ipconfig", "network:windows:config", "windows",
     "Displays TCP/IP network configuration and refreshes DHCP/DNS.",
     None, ["windows"], ["T1015"]),
    ("tracert", "tracert", "network:diagnostic:trace", "windows",
     "Traces the route packets take to a network destination.",
     None, ["windows"], ["T1046"]),
    ("pathping", "pathping", "network:diagnostic:latency", "windows",
     "Combines ping and tracert with packet loss per hop.",
     None, ["windows"], []),
    ("netstat", "netstat", "network:monitoring:connections", "network",
     "Displays active connections, listening ports, and routing tables.",
     None, ["linux","windows"], ["T1049"]),
    ("nbtstat", "nbtstat", "network:netbios:stats", "windows",
     "Displays NetBIOS over TCP/IP statistics and name tables.",
     None, ["windows"], []),
    ("getmac", "getmac", "network:interface:mac", "windows",
     "Returns MAC addresses of network adapters.",
     None, ["windows"], []),
    ("diskpart", "diskpart", "system:windows:disk", "windows",
     "Disk partitioning utility for managing disks and volumes.",
     None, ["windows"], []),
    ("chkdsk", "chkdsk", "system:windows:disk", "windows",
     "Checks disks for file system errors and bad sectors.",
     None, ["windows"], []),
    ("sfc", "sfc", "system:windows:integrity", "windows",
     "System File Checker scans and repairs protected system files.",
     None, ["windows"], []),
    ("msg", "msg", "system:windows:communication", "windows",
     "Sends popup messages to users on local or remote machines.",
     None, ["windows"], []),
    ("klist", "klist", "security:kerberos:tickets", "windows",
     "Lists cached Kerberos tickets for authentication.",
     None, ["windows"], ["T1558"]),
    ("ksetup", "ksetup", "security:kerberos:config", "windows",
     "Configures Kerberos realm mappings and encryption types.",
     None, ["windows"], []),
    ("repadmin", "repadmin", "security:ad:replication", "windows",
     "Active Directory replication diagnostics and management.",
     None, ["windows"], []),
    ("dcdiag", "dcdiag", "security:ad:diagnostic", "windows",
     "Domain Controller diagnostics for AD analysis.",
     None, ["windows"], []),
    ("nltest", "nltest", "security:ad:trust", "windows",
     "Queries and manages AD trust relationships.",
     None, ["windows"], []),
    ("dsquery", "dsquery", "security:ad:query", "windows",
     "Queries Active Directory for matching objects.",
     None, ["windows"], []),
    ("csvde", "csvde", "security:ad:export", "windows",
     "Imports/exports AD objects using CSV format.",
     None, ["windows"], []),
    ("logman", "logman", "system:windows:monitor", "windows",
     "Manages Performance Monitor logs and data collector sets.",
     None, ["windows"], []),
    ("mstsc", "mstsc", "remote:rdp:client", "windows",
     "Remote Desktop Connection client.",
     None, ["windows"], []),
    ("winrs", "winrs", "remote:winrm:shell", "windows",
     "Windows Remote Shell via WinRM.",
     None, ["windows"], []),
    ("qwinsta", "qwinsta", "remote:ts:query", "windows",
     "Displays Remote Desktop Services sessions on a server.",
     None, ["windows"], []),
    ("tscon", "tscon", "remote:ts:connect", "windows",
     "Connects a Remote Desktop session to a different session.",
     None, ["windows"], ["T1563"]),
    ("tsdiscon", "tsdiscon", "remote:ts:disconnect", "windows",
     "Disconnects a Remote Desktop Services session.",
     None, ["windows"], []),
    ("bootcfg", "bootcfg", "system:windows:boot", "windows",
     "Configures Boot.ini for multi-boot systems.",
     None, ["windows"], []),
    ("typeperf", "typeperf", "system:windows:performance", "windows",
     "Writes performance counter data to command line or log.",
     None, ["windows"], []),
    ("lodctr", "lodctr", "system:windows:performance", "windows",
     "Registers performance counter names for services.",
     None, ["windows"], []),
    ("winver", "winver", "system:windows:info", "windows",
     "Displays Windows version and build information.",
     None, ["windows"], []),
    ("reagentc", "reagentc", "system:windows:recovery", "windows",
     "Windows Recovery Environment configuration tool.",
     None, ["windows"], []),
    ("recdisc", "recdisc", "system:windows:recovery", "windows",
     "Creates a system repair disc.",
     None, ["windows"], []),
    ("rwinsta", "rwinsta", "remote:ts:reset", "windows",
     "Resets a Remote Desktop Services session.",
     None, ["windows"], []),
    
    # Linux basics
    ("lsof", "lsof", "system:linux:process", "system",
     "Lists open files and the processes that opened them.",
     "custom", ["linux","macos"], []),
    ("fuser", "fuser", "system:linux:process", "system",
     "Identifies processes using files or sockets.",
     "custom", ["linux","macos"], []),
    ("readlink", "readlink", "system:linux:file", "system",
     "Displays the target of a symbolic link.",
     None, ["linux","macos"], []),
    ("xclip", "xclip", "system:linux:clipboard", "system",
     "CLI interface to the X11 clipboard.",
     "custom", ["linux"], []),
    ("nmcli", "nmcli", "network:linux:config", "network",
     "NetworkManager command-line client.",
     "custom", ["linux"], []),
    ("host", "host", "network:dns:lookup", "network",
     "Simple DNS lookup for forward and reverse lookups.",
     "custom", ["linux","macos"], ["T1590"]),
    ("strace", "strace", "system:linux:trace", "system",
     "System call tracer for Linux.",
     "custom", ["linux"], []),
    ("htop", "htop", "system:linux:monitor", "system",
     "Interactive process viewer and manager.",
     "custom", ["linux","macos"], []),
    ("ethtool", "ethtool", "network:linux:interface", "network",
     "Displays and changes Ethernet device settings.",
     "custom", ["linux"], []),
    ("useradd", "useradd", "system:linux:user", "system",
     "Creates a new user account with home directory, shell, and groups.",
     None, ["linux"], []),
    ("gunzip", "gunzip", "archive:linux:compression", "archive",
     "Decompresses gzip-compressed (.gz) files.",
     None, ["linux","macos"], []),
    ("getfacl", "getfacl", "system:linux:permissions", "system",
     "Gets file access control lists (ACLs).",
     None, ["linux"], []),
    ("lsattr", "lsattr", "system:linux:filesystem", "system",
     "Lists file attributes on ext2/ext3/ext4 filesystems.",
     None, ["linux"], []),
    ("tcpflow", "tcpflow", "network:capture:traffic", "network",
     "Captures TCP connections and reconstructs data streams.",
     "custom", ["linux"], []),
    ("tcpreplay", "tcpreplay", "network:capture:traffic", "network",
     "Replays pcap network traffic for device testing.",
     "custom", ["linux"], []),
    
    # Pentesting tools - network/service enumeration
    ("smbclient", "smbclient", "security:smb:client", "security",
     "SMB/CIFS client for accessing SMB shares on remote servers.",
     "custom", ["linux"], ["T1021"]),
    ("smbmap", "smbmap", "security:smb:enumeration", "security",
     "SMB enumeration tool for share drives, permissions, and directory contents.",
     "custom", ["linux"], []),
    ("enum4linux", "enum4linux", "security:smb:enumeration", "security",
     "Enumerates SMB/NetBIOS information from Windows systems.",
     "custom", ["linux"], []),
    ("rpcclient", "rpcclient", "security:rpc:client", "security",
     "SMB/CIFS RPC client for MS-RPC protocol operations.",
     "custom", ["linux"], []),
    ("crackmapexec", "crackmapexec", "security:network:exploit", "security",
     "Swiss Army knife for network service exploitation (SMB, WinRM, MSSQL, SSH, LDAP).",
     "custom", ["linux"], []),
    ("ldapsearch", "ldapsearch", "security:ldap:query", "security",
     "LDAP search tool for querying directory services.",
     "custom", ["linux"], []),
    ("ldapdomaindump", "ldapdomaindump", "security:ldap:dump", "security",
     "Dumps LDAP domain information from Active Directory.",
     "custom", ["linux"], []),
    ("bloodhound-python", "bloodhound-python", "security:ad:analyze", "security",
     "BloodHound Python ingestor for Active Directory relationships.",
     "custom", ["linux"], []),
    ("ligolo-ng", "ligolo-ng", "network:tunnel:proxy", "network",
     "Tunneling/pivoting proxy for network penetration testing.",
     "custom", ["linux"], []),
    
    # Privilege escalation tools
    ("pspy", "pspy", "security:linux:monitor", "security",
     "Process monitor for Linux privilege escalation detection.",
     "custom", ["linux"], []),
    ("linpeas", "linpeas", "security:linux:enumeration", "security",
     "Linux local privilege escalation enumeration and auditing script.",
     "custom", ["linux"], []),
    ("winpeas", "winpeas", "security:windows:enumeration", "security",
     "Windows local privilege escalation enumeration and auditing script.",
     "custom", ["windows"], []),
    
    # Impacket tools
    ("impacket-smbexec", "impacket-smbexec", "security:impacket:execution", "security",
     "Impacket SMBexec - executes commands via SMB protocol.",
     "custom", ["linux"], ["T1047"]),
    ("impacket-psexec", "impacket-psexec", "security:impacket:execution", "security",
     "Impacket PsExec - executes processes on remote Windows systems.",
     "custom", ["linux"], ["T1047"]),
    ("impacket-wmiexec", "impacket-wmiexec", "security:impacket:execution", "security",
     "Impacket WMIexec - executes commands via WMI protocol.",
     "custom", ["linux"], ["T1047"]),
    ("impacket-secretsdump", "impacket-secretsdump", "security:impacket:credential", "security",
     "Impacket secretsdump - extracts secrets from Windows systems.",
     "custom", ["linux"], ["T1003"]),
    ("impacket-mssqlexec", "impacket-mssqlexec", "security:impacket:database", "security",
     "Impacket MSSQLexec - executes commands via MSSQL server.",
     "custom", ["linux"], []),
    ("impacket-atexec", "impacket-atexec", "security:impacket:execution", "security",
     "Impacket ATexec - executes commands via Windows Task Scheduler.",
     "custom", ["linux"], ["T1053"]),
    ("impacket-dcomexec", "impacket-dcomexec", "security:impacket:execution", "security",
     "Impacket DCOMexec - executes commands via DCOM protocol.",
     "custom", ["linux"], ["T1047"]),
    ("impacket-getTGT", "impacket-getTGT", "security:impacket:kerberos", "security",
     "Gets Kerberos Ticket Granting Tickets (TGT) from a KDC.",
     "custom", ["linux"], ["T1558"]),
    ("impacket-getST", "impacket-getST", "security:impacket:kerberos", "security",
     "Gets Kerberos Service Tickets using credentials.",
     "custom", ["linux"], ["T1558"]),
    ("impacket-ticketer", "impacket-ticketer", "security:impacket:kerberos", "security",
     "Creates golden/silver Kerberos tickets.",
     "custom", ["linux"], ["T1558"]),
    ("impacket-samrdump", "impacket-samrdump", "security:impacket:credential", "security",
     "Dumps SAM (Security Account Manager) information from remote systems.",
     "custom", ["linux"], ["T1003"]),
    ("impacket-rpcdump", "impacket-rpcdump", "security:impacket:enumeration", "security",
     "Dumps RPC endpoint information from remote systems.",
     "custom", ["linux"], []),
    ("impacket-reg", "impacket-reg", "security:impacket:registry", "security",
     "Remote registry manipulation tool from Impacket.",
     "custom", ["linux"], []),
]

CAPS = {
    "windows": ["system.information-gathering", "system.configuration", "system.administration"],
    "network": ["network.diagnostics", "network.configuration", "system.information-gathering"],
    "system": ["system.information-gathering", "system.monitoring", "system.administration"],
    "remote": ["remote-access.client", "network.connection", "system.authentication"],
    "security": ["security.authentication", "security.auditing", "security.directory-services"],
    "archive": ["filesystem.compression", "filesystem.management", "system.commands"],
}

INSTALL_CMDS = {
    "lsof": "apt-get install -y lsof",
    "fuser": "apt-get install -y psmisc",
    "xclip": "apt-get install -y xclip",
    "host": "apt-get install -y bind9-dnsutils",
    "strace": "apt-get install -y strace",
    "htop": "apt-get install -y htop",
    "ethtool": "apt-get install -y ethtool",
    "nmcli": "apt-get install -y network-manager",
    "nslookup": "apt-get install -y dnsutils",
    "tcpflow": "apt-get install -y tcpflow",
    "tcpreplay": "apt-get install -y tcpreplay",
    "smbclient": "apt-get install -y smbclient",
    "smbmap": "apt-get install -y smbmap",
    "enum4linux": "apt-get install -y enum4linux",
    "rpcclient": "apt-get install -y smbclient",
    "crackmapexec": "pipx install crackmapexec",
    "ldapsearch": "apt-get install -y ldap-utils",
    "ldapdomaindump": "pipx install ldapdomaindump",
    "bloodhound-python": "pipx install bloodhound",
    "ligolo-ng": "go install github.com/nicocha30/ligolo-ng/cmd/ligolo-agent@latest",
    "pspy": "wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspy64",
    "linpeas": "curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh",
    "winpeas": "curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEAS.bat",
    "impacket-smbexec": "pipx install impacket",
    "impacket-psexec": "pipx install impacket",
    "impacket-wmiexec": "pipx install impacket",
    "impacket-secretsdump": "pipx install impacket",
    "impacket-mssqlexec": "pipx install impacket",
    "impacket-atexec": "pipx install impacket",
    "impacket-dcomexec": "pipx install impacket",
    "impacket-getTGT": "pipx install impacket",
    "impacket-getST": "pipx install impacket",
    "impacket-ticketer": "pipx install impacket",
    "impacket-samrdump": "pipx install impacket",
    "impacket-rpcdump": "pipx install impacket",
    "impacket-reg": "pipx install impacket",
}

def generated(entry):
    tool_id, name, namespace, domain, desc, install_method, platforms, mitre = entry
    caps = CAPS.get(domain, CAPS["system"])
    fm_id = tool_id.lower()
    if "-" not in fm_id:
        prefix_map = {
            "windows": "cmd",
            "network": "net",
            "system": "sys",
            "remote": "rmt",
            "security": "sec",
            "archive": "arc",
        }
        prefix = prefix_map.get(tool_id, "cmd")
        fm_id = f"{prefix}-{fm_id}"

    exec_descriptions = {
        "set": ("set", "Display all environment variables"),
        "dir": ("dir .", "List files in current directory"),
        "netstat": ("netstat", "Display active network connections"),
        "hostname": ("hostname", "Display system hostname"),
        "systeminfo": ("systeminfo", "Display system information"),
        "nslookup": ("nslookup example.com", "Query DNS for a domain"),
        "host": ("host example.com", "Lookup DNS records"),
        "lsof": ("lsof", "List open files"),
        "htop": ("htop", "Interactive process viewer"),
        "msg": ('msg /server:localhost "test message"', "Send a test message"),
    }

    if tool_id in exec_descriptions:
        exec_tpl, ex_desc = exec_descriptions[tool_id]
    elif domain == "windows":
        exec_tpl = f"{name} /?"
        ex_desc = f"Display help for {name}"
    else:
        exec_tpl = f"{name} --help"
        ex_desc = f"Display help for {name}"

    fm = {
        "id": fm_id,
        "namespace": namespace,
        "name": name,
        "description": desc,
        "version": "1.0.0",
        "capabilities": caps,
        "platforms": platforms,
        "features": ["local"],
        "mitre_ids": mitre,
        "parameters": [],
        "execution": {
            "template": exec_tpl,
            "sandbox": "execFile",
        },
        "examples": [
            {"description": ex_desc, "command": exec_tpl}
        ],
        "references": [
            {
                "label": f"{name} Documentation",
                "url": f"https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/{name}",
            }
        ],
    }

    if install_method:
        cmds = [INSTALL_CMDS.get(tool_id, f"apt-get install -y {tool_id}")]
        fm["install"] = [{"method": "custom", "description": "Install via package manager", "commands": cmds}]

    man8 = ["ethtool", "netstat"]
    man1 = ["lsof", "fuser", "strace", "host"]
    if tool_id in man8:
        fm["references"].append({"label": f"{name} manual", "url": f"https://man7.org/linux/man-pages/man8/{tool_id}.8.html"})
    elif tool_id in man1:
        fm["references"].append({"label": f"{name} manual", "url": f"https://man7.org/linux/man-pages/man1/{tool_id}.1.html"})

    yaml_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{yaml_str}---\n"

def main():
    dry = "--dry-run" in sys.argv
    created = skipped = 0
    for entry in NEW_TOOLS:
        fpath = TOOLS_DIR / f"{entry[0]}.md"
        if fpath.exists():
            skipped += 1
            continue
        if dry:
            print(f"[DRY] {entry[0]}.md")
        else:
            fpath.write_text(generated(entry))
            print(f"[OK] {entry[0]}.md")
        created += 1
    print(f"\n{created} created, {skipped} skipped")

if __name__ == "__main__":
    main()
