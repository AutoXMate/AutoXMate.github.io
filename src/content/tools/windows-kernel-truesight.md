---
id: windows-kernel-truesight
namespace: windows:kernel:truesight
name: "truesight.sys"
description: "This is a C# AV/EDR Killer using Rogue Anti-Malware Driver 3.3. This driver is not present in the loldrivers or Windows blocklist at the time of this writing. The only reason I'm making this public is because the company has already published a fix in version 3.4, and Microsoft will likely block this driver soon. This driver can be used in Windows 23H2 with HVCI enabled, loldrivers blocklist, or WDAC enabled. HVCI is designed to ensure the integrity of code executed in the kernel, but it cann..."
author: "ph4nt0mbyt3, Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: "sc.exe create truesight.sys binPath=C:\\windows\\temp\\truesight.sys type=kernel && sc.exe start truesight.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load truesight.sys kernel driver"
    commands:
      - "sc.exe create truesight.sys binPath=C:\\windows\\temp\\truesight.sys type=kernel && sc.exe start truesight.sys"
references:
  - label: "Reference"
    url: "https://github.com/ph4nt0mbyt3/Darkside"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create truesight.sys binPath=C:\\\\windows\\\\temp\\\\truesight.sys type=kernel && sc.exe start truesight.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver truesight.sys"

# truesight.sys

This is a C# AV/EDR Killer using Rogue Anti-Malware Driver 3.3. This driver is not present in the loldrivers or Windows blocklist at the time of this writing. The only reason I'm making this public is because the company has already published a fix in version 3.4, and Microsoft will likely block this driver soon. This driver can be used in Windows 23H2 with HVCI enabled, loldrivers blocklist, or WDAC enabled. HVCI is designed to ensure the integrity of code executed in the kernel, but it cannot protect against all possible vulnerabilities or actions that can be performed through drivers or system interfaces.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068