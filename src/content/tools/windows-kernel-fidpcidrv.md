---
id: windows-kernel-fidpcidrv
namespace: windows:kernel:fidpcidrv
name: "fidpcidrv.sys"
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
trust_level: community
execution:
  template: "sc.exe create fidpcidrv.sys binPath=C:\\windows\\temp\\fidpcidrv.sys type=kernel && sc.exe start fidpcidrv.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load fidpcidrv.sys kernel driver"
    commands:
      - "sc.exe create fidpcidrv.sys binPath=C:\\windows\\temp\\fidpcidrv.sys type=kernel && sc.exe start fidpcidrv.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create fidpcidrv.sys binPath=C:\\\\windows\\\\temp\\\\fidpcidrv.sys type=kernel && sc.exe start fidpcidrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver fidpcidrv.sys"

# fidpcidrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068