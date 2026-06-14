---
id: windows-kernel-t8
namespace: windows:kernel:t8
name: "t8.sys"
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
  template: "sc.exe create t8.sys binPath=C:\\windows\\temp\\t8.sys type=kernel && sc.exe start t8.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load t8.sys kernel driver"
    commands:
      - "sc.exe create t8.sys binPath=C:\\windows\\temp\\t8.sys type=kernel && sc.exe start t8.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create t8.sys binPath=C:\\\\windows\\\\temp\\\\t8.sys type=kernel && sc.exe start t8.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver t8.sys"

# t8.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068