---
id: windows-kernel-blackbonedrv10
namespace: windows:kernel:blackbonedrv10
name: "BlackBoneDrv10.sys"
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
  template: "sc.exe create BlackBoneDrv10.sys binPath=C:\\windows\\temp\\BlackBoneDrv10.sys     type=kernel && sc.exe start BlackBoneDrv10.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load BlackBoneDrv10.sys kernel driver"
    commands:
      - "sc.exe create BlackBoneDrv10.sys binPath=C:\\windows\\temp\\BlackBoneDrv10.sys     type=kernel && sc.exe start BlackBoneDrv10.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BlackBoneDrv10.sys binPath=C:\\\\windows\\\\temp\\\\BlackBoneDrv10.sys     type=kernel && sc.exe start BlackBoneDrv10.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BlackBoneDrv10.sys"

# BlackBoneDrv10.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068