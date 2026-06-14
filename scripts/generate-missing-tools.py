#!/usr/bin/env python3
"""
AutoXMate Batch Tool Generator
Generates new tool entries for missing CLI commands with proper frontmatter.
"""

import os
import sys
import yaml
from pathlib import Path

TOOLS_DIR = Path("/home/shell/Apps/Shell/AutoMate/AutoXMate/src/content/tools")

# Define new tools to add: (id, name, namespace, domain, description, install_method, install_cmd, mitre_ids)
NEW_TOOLS = [
    # Windows CMD commands (from hacktricks/Windows pentesting)
    ("systeminfo", "systeminfo", "system:windows:cmd", "windows",
     "Displays detailed operating system configuration information including OS version, build number, service pack level, and system hardware specs.",
     "native", "", []),
    ("hostname", "hostname", "system:windows:cmd", "windows",
     "Displays the host name portion of the full computer name of the computer.",
     "native", "", []),
    ("driverquery", "driverquery", "system:windows:driver", "windows",
     "Displays a list of all installed device drivers and their properties including driver name, type, and module name.",
     "native", "", []),
    ("set", "set", "system:windows:cmd", "windows",
     "Displays, sets, or removes environment variables. Used without parameters, displays all current environment variables.",
     "native", "", []),
    ("nslookup", "nslookup", "network:dns", "network",
     "Queries DNS servers for domain name or IP address resolution. Supports interactive and non-interactive modes.",
     "apt", "apt-get install -y dnsutils", ["T1590"]),
    ("tasklist", "tasklist", "system:windows:process", "windows",
     "Displays a list of currently running processes on the local or remote machine with PID, session name, and memory usage.",
     "native", "", ["T1057"]),
    ("net", "net", "system:windows:networking", "windows",
     "Comprehensive network and system administration command used for managing users, groups, shares, services, and network connections.",
     "native", "", []),
    ("where", "where", "system:windows:file", "windows",
     "Displays the location of files that match the search pattern, similar to Unix 'which' but with broader search capabilities.",
     "native", "", []),
    ("dir", "dir", "system:windows:file", "windows",
     "Displays a list of files and subdirectories in a directory. Supports various sorting and filtering options.",
     "native", "", []),
    ("wevtutil", "wevtutil", "system:windows:logging", "windows",
     "Retrieves information about event logs and publishers, exports, archives, and clears event logs.",
     "native", "", []),
    ("gpresult", "gpresult", "system:windows:policy", "windows",
     "Displays the Resultant Set of Policy (RSoP) information for a target user and computer including applied GPOs.",
     "native", "", []),
    ("shutdown", "shutdown", "system:windows:admin", "windows",
     "Allows shutdown, restart, or logoff of local or remote computers with scheduled timing and comment support.",
     "native", "", []),
    ("bcdedit", "bcdedit", "system:windows:boot", "windows",
     "Boot Configuration Data (BCD) editor for managing boot configuration and troubleshooting startup issues.",
     "native", "", []),
    ("vssadmin", "vssadmin", "system:windows:backup", "windows",
     "Volume Shadow Copy Service administration tool for managing shadow copies, providers, and volumes.",
     "native", "", []),
    ("wusa", "wusa", "system:windows:update", "windows",
     "Windows Update Standalone Installer for installing, uninstalling, and listing Windows update packages.",
     "native", "", []),
    ("ipconfig", "ipconfig", "network:windows:config", "windows",
     "Displays all current TCP/IP network configuration values and refreshes DHCP and DNS settings.",
     "native", "", ["T1015"]),
    ("tracert", "tracert", "network:diagnostic", "windows",
     "Traces the route packets take to a network destination by sending ICMP echo requests with incrementing TTL values.",
     "native", "", ["T1046"]),
    ("pathping", "pathping", "network:diagnostic", "windows",
     "Combines ping and tracert functionality to provide packet loss information and latency at each hop.",
     "native", "", []),
    ("netstat", "netstat", "network:monitoring", "network",
     "Displays active TCP connections, listening ports, routing tables, and network protocol statistics.",
     "native", "", ["T1049"]),
    ("nbtstat", "nbtstat", "network:netbios", "windows",
     "Displays NetBIOS over TCP/IP protocol statistics, name tables, and cache information for local and remote machines.",
     "native", "", []),
    ("getmac", "getmac", "network:interface", "windows",
     "Returns the MAC address (physical address) of network adapters on the system.",
     "native", "", []),
    ("winver", "winver", "system:windows:info", "windows",
     "Displays a dialog box showing the current Windows version, build number, and system information.",
     "native", "", []),
    ("logman", "logman", "system:windows:performance", "windows",
     "Manages Performance Monitor logs and traces. Creates, starts, stops, and queries performance data collector sets.",
     "native", "", []),
    ("diskpart", "diskpart", "system:windows:disk", "windows",
     "Command-line disk partitioning utility for managing disks, partitions, volumes, and virtual hard disks.",
     "native", "", []),
    ("chkdsk", "chkdsk", "system:windows:disk", "windows",
     "Checks a disk for file system errors and bad sectors. Can attempt repairs with appropriate flags.",
     "native", "", []),
    ("sfc", "sfc", "system:windows:integrity", "windows",
     "System File Checker scans and verifies protected system files, replacing corrupted versions from the cache.",
     "native", "", []),
    ("bootcfg", "bootcfg", "system:windows:boot", "windows",
     "Configures, queries, or changes Boot.ini file settings for multi-boot systems.",
     "native", "", []),
    ("reagentc", "reagentc", "system:windows:recovery", "windows",
     "Windows Recovery Environment configuration tool for enabling/disabling WinRE and setting recovery image paths.",
     "native", "", []),
    ("msg", "msg", "system:windows:communication", "windows",
     "Sends popup messages to users on local or remote machines via the Messenger service.",
     "native", "", []),
    ("klist", "klist", "security:kerberos", "windows",
     "Displays the list of currently cached Kerberos tickets for authentication purposes.",
     "native", "", ["T1558"]),
    ("ksetup", "ksetup", "security:kerberos", "windows",
     "Configures Kerberos settings including realm mappings, keytab files, and encryption types.",
     "native", "", []),
    ("repadmin", "repadmin", "security:ad:replication", "windows",
     "Active Directory replication diagnostics and management tool for monitoring and troubleshooting AD replication.",
     "native", "", []),
    ("dcdiag", "dcdiag", "security:ad:diagnostic", "windows",
     "Domain Controller diagnostics tool that analyzes the state of domain controllers in an Active Directory forest.",
     "native", "", []),
    ("nltest", "nltest", "security:ad:trust", "windows",
     "Network test tool for querying and managing Active Directory trust relationships and secure channels.",
     "native", "", []),
    ("dsquery", "dsquery", "security:ad:query", "windows",
     "Active Directory query tool that retrieves objects from the directory using specified criteria.",
     "native", "", []),
    ("csvde", "csvde", "security:ad:export", "windows",
     "Imports and exports Active Directory objects using comma-separated-value (CSV) format files.",
     "native", "", []),
    ("typeperf", "typeperf", "system:windows:performance", "windows",
     "Performance monitoring tool that writes performance counter data to the command window or a log file.",
     "native", "", []),
    ("lodctr", "lodctr", "system:windows:performance", "windows",
     "Allows registering or unregistering performance counter names and explanation text for system services.",
     "native", "", []),
    ("mstsc", "mstsc", "remote:rdp", "windows",
     "Remote Desktop Connection client for connecting to remote Windows desktops and applications.",
     "native", "", []),
    ("winrs", "winrs", "remote:winrm", "windows",
     "Windows Remote Shell allows running commands on remote Windows machines via WinRM protocol.",
     "native", "", []),
    ("recdisc", "recdisc", "system:windows:recovery", "windows",
     "Creates a system repair disc that can be used to boot into Windows Recovery Environment.",
     "native", "", []),
    ("rwinsta", "rwinsta", "remote:ts", "windows",
     "Resets (logs off) a Remote Desktop Services session on a remote server.",
     "native", "", []),
    ("qwinsta", "qwinsta", "remote:ts", "windows",
     "Displays information about Remote Desktop Services sessions on a remote server.",
     "native", "", []),
    ("tscon", "tscon", "remote:ts", "windows",
     "Connects a Remote Desktop Services session to a different session, enabling session hijacking.",
     "native", "", ["T1563"]),
    ("tsdiscon", "tsdiscon", "remote:ts", "windows",
     "Disconnects a Remote Desktop Services session without ending the session.",
     "native", "", []),
    
    # Linux basics (from hacktricks)
    ("lsof", "lsof", "system:linux:process", "system",
     "Lists open files and the processes that opened them. Useful for finding which processes have specific files or network connections open.",
     "apt", "apt-get install -y lsof", []),
    ("fuser", "fuser", "system:linux:process", "system",
     "Identifies processes using files or sockets. Can kill processes that have a file open.",
     "apt", "apt-get install -y psmisc", []),
    ("readlink", "readlink", "system:linux:file", "system",
     "Displays the target of a symbolic link or canonical path. Useful for resolving file paths and following symlinks.",
     "native", "", []),
    ("xclip", "xclip", "system:linux:clipboard", "system",
     "Command-line interface to the X11 clipboard. Pipes data to/from the clipboard selection buffers.",
     "apt", "apt-get install -y xclip", []),
    ("useradd", "useradd", "system:linux:user", "system",
     "Creates a new user account on the system with specified options for home directory, shell, groups, and expiry.",
     "native", "", []),
    ("gunzip", "gunzip", "archive:compression", "archive",
     "Decompresses files compressed with gzip (.gz). Equivalent to gzip -d.",
     "native", "", []),
    ("nmcli", "nmcli", "network:linux:manager", "network",
     "Command-line client for NetworkManager. Manages network connections, devices, and Wi-Fi from the terminal.",
     "apt", "apt-get install -y network-manager", []),
    ("host", "host", "network:dns", "network",
     "Simple DNS lookup utility that performs forward and reverse DNS lookups.",
     "apt", "apt-get install -y bind9-host", ["T1590"]),
    ("strace", "strace", "system:linux:trace", "system",
     "System call tracer for Linux. Intercepts and records system calls made by a process.",
     "apt", "apt-get install -y strace", []),
    ("getfacl", "getfacl", "system:linux:permissions", "system",
     "Gets file access control lists (ACLs). Displays the ACL entries for one or more files.",
     "native", "", []),
    ("lsattr", "lsattr", "system:linux:file", "system",
     "Lists file attributes on a Linux ext2/ext3/ext4 file system.",
     "native", "", []),
    ("htop", "htop", "system:linux:monitor", "system",
     "Interactive process viewer and manager. An enhanced version of top with color output and mouse support.",
     "apt", "apt-get install -y htop", []),
    ("ethtool", "ethtool", "network:interface", "network",
     "Displays and changes Ethernet device settings including speed, duplex, auto-negotiation, and driver info.",
     "apt", "apt-get install -y ethtool", []),
    ("tcpflow", "tcpflow", "network:capture", "network",
     "TCP flow recorder that captures TCP connections and reconstructs the data streams for analysis.",
     "apt", "apt-get install -y tcpflow", []),
    ("tcpreplay", "tcpreplay", "network:capture", "network",
     "Replays captured network traffic from pcap files, allowing testing of network devices and IDS/IPS systems.",
     "apt", "apt-get install -y tcpreplay", []),
]

TEMPLATE = """---
id: {id}
namespace: {namespace}
name: {name}
description: {desc}
version: "1.0.0"
capabilities:
  - {cap1}
  - {cap2}
  - {cap3}
features:
  - local
install:
  - method: {install_method}
    commands:
      - "{install_cmd}"
  - method: native
    commands:
      - "{native_help}"
mitre_ids: {mitre_ref}
parameters: []
execution:
  method: {exec_method}
  templates:
    - template: |
        {exec_example}
  background_templates: []
examples:
  - cmd: "{example_cmd_short}"
    description: "{example_desc}"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/{name}
  - https://www.man7.org/linux/man-pages/man1/{id}.1.html
"""

def generate_tool(entry):
    """Generate a tool markdown file."""
    tool_id, name, namespace, domain, desc, install_method, install_cmd, mitre = entry
    
    # Determine capabilities based on domain
    if domain == "windows":
        cap1 = "windows-command"
        cap2 = "system-administration"
        cap3 = "information-gathering"
        exec_method = "cmd"
        exec_example = f"{name} /?"
        native_help = f"{name} /?"
    elif domain == "network":
        cap1 = "network-diagnostics"
        cap2 = "information-gathering"
        cap3 = "reconnaissance"
        exec_method = "cmd"
        exec_example = f"{name} --help"
        native_help = f"{name} --help"
    elif domain == "system":
        cap1 = "system-administration"
        cap2 = "information-gathering"
        cap3 = "file-system"
        exec_method = "shell"
        exec_example = f"{name} --help"
        native_help = f"{name} --help"
    elif domain == "archive":
        cap1 = "compression"
        cap2 = "file-system"
        cap3 = "data-transfer"
        exec_method = "shell"
        exec_example = f"{name} --help"
        native_help = f"{name} --help"
    elif domain == "remote":
        cap1 = "remote-access"
        cap2 = "authentication"
        cap3 = "network-connection"
        exec_method = "cmd"
        exec_example = f"{name} /?"
        native_help = f"{name} /?"
    elif domain == "security":
        cap1 = "security-auditing"
        cap2 = "authentication"
        cap3 = "information-gathering"
        exec_method = "cmd"
        exec_example = f"{name} /?"
        native_help = f"{name} /?"
    else:
        cap1 = "information-gathering"
        cap2 = "system-administration"
        cap3 = "automation"
        exec_method = "shell"
        exec_example = f"{name} --help"
        native_help = f"{name} --help"
    
    # Execution example
    if tool_id in ["netstat", "tasklist", "systeminfo"]:
        exec_example = f"{name}"
    elif tool_id in ["set"]:
        exec_example = f"{name}"
        native_help = f"{name}"
    elif tool_id in ["dir", "where"]:
        exec_example = f"{name} ."
    elif tool_id in ["logman", "typeperf", "lodctr"]:
        exec_example = f"{name} /?"
    elif tool_id in ["msg"]:
        exec_example = f'{name} /server:localhost "test message"'
    elif tool_id in ["rwinsta", "qwinsta", "tscon", "tsdiscon"]:
        exec_example = f"{name} /?"
    
    # Short example
    example_cmd = f"{name} /?" if domain in ["windows", "remote"] else f"{name} --help"
    example_desc = f"Display help and usage information for {name}"
    
    if tool_id == "set":
        example_cmd = f"{name}"
        example_desc = "Display all environment variables"
    elif tool_id == "dir":
        example_cmd = f"{name} /b"
        example_desc = "List files in bare format"
    elif tool_id == "netstat":
        example_cmd = f"{name} -an"
        example_desc = "Display all active connections and listening ports"
    elif tool_id == "tasklist":
        example_cmd = f"{name} /V"
        example_desc = "Display verbose task listing"
    elif tool_id == "systeminfo":
        example_cmd = f"{name}"
        example_desc = "Display system information"
    elif tool_id == "ipconfig":
        example_cmd = f"{name} /all"
        example_desc = "Display full TCP/IP configuration"
    elif tool_id == "nslookup":
        example_cmd = f'{name} example.com'
        example_desc = "Query DNS for a domain"
    elif tool_id == "host":
        example_cmd = f'{name} example.com'
        example_desc = "Lookup DNS records for a domain"
    elif tool_id == "net":
        example_cmd = f'{name} user'
        example_desc = "List user accounts"
    elif tool_id in ["lsof", "fuser", "strace"]:
        example_cmd = f"{name} -h"
        example_desc = f"Display help for {name}"
    
    # Build the file content
    content = f"""---
id: {tool_id}
namespace: {namespace}
name: {name}
description: {desc}
version: "1.0.0"
capabilities:
  - {cap1}
  - {cap2}
  - {cap3}
features:
  - local
  - batch
install:
  - method: {install_method}
    commands:
      - "{install_cmd}"
mitre_ids: []
parameters: []
execution:
  method: {exec_method}
  templates:
    - template: |
        {name}
  background_templates: []
examples:
  - cmd: "{exec_example}"
    description: "{example_desc}"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/{name}
---"""
    
    return content

def main():
    dry_run = "--dry-run" in sys.argv
    
    created = 0
    skipped = 0
    
    for entry in NEW_TOOLS:
        tool_id = entry[0]
        fpath = TOOLS_DIR / f"{tool_id}.md"
        
        if fpath.exists():
            skipped += 1
            continue
        
        content = generate_tool(entry)
        
        if dry_run:
            print(f"[DRY-RUN] Would create: {fpath.name}")
        else:
            fpath.write_text(content)
            print(f"[CREATED] {fpath.name}")
        
        created += 1
    
    print(f"\nSummary: {created} created, {skipped} skipped")
    if dry_run:
        print("Run without --dry-run to apply")

if __name__ == "__main__":
    main()
