---
id: windows-kernel-d4
namespace: windows:kernel:d4
name: "d4.sys"
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
  template: "sc.exe create d4.sys binPath=C:\\windows\\temp\\d4.sys type=kernel && sc.exe start d4.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load d4.sys kernel driver"
    commands:
      - "sc.exe create d4.sys binPath=C:\\windows\\temp\\d4.sys type=kernel && sc.exe start d4.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create d4.sys binPath=C:\\\\windows\\\\temp\\\\d4.sys type=kernel && sc.exe start d4.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver d4.sys"

# d4.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068