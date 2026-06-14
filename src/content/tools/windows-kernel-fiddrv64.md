---
id: windows-kernel-fiddrv64
namespace: windows:kernel:fiddrv64
name: "fiddrv64.sys"
description: "Elevate privileges"
author: "Michael Haag"
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
  template: "sc.exe create fiddrv64.sys binPath=C:\\windows\\temp\\fiddrv64.sys type=kernel && sc.exe start fiddrv64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load fiddrv64.sys kernel driver"
    commands:
      - "sc.exe create fiddrv64.sys binPath=C:\\windows\\temp\\fiddrv64.sys type=kernel && sc.exe start fiddrv64.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create fiddrv64.sys binPath=C:\\\\windows\\\\temp\\\\fiddrv64.sys type=kernel && sc.exe start fiddrv64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver fiddrv64.sys"

# fiddrv64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068