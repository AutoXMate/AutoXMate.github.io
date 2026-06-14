---
id: windows-kernel-81
namespace: windows:kernel:81
name: "81.sys"
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
  template: "sc.exe create 81.sys binPath=C:\\windows\\temp\\81.sys type=kernel && sc.exe start 81.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load 81.sys kernel driver"
    commands:
      - "sc.exe create 81.sys binPath=C:\\windows\\temp\\81.sys type=kernel && sc.exe start 81.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 81.sys binPath=C:\\\\windows\\\\temp\\\\81.sys type=kernel && sc.exe start 81.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 81.sys"

# 81.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068