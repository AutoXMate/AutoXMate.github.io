---
id: windows-kernel-80
namespace: windows:kernel:80
name: "80.sys"
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
  template: "sc.exe create 80.sys binPath=C:\\windows\\temp\\80.sys type=kernel && sc.exe start 80.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load 80.sys kernel driver"
    commands:
      - "sc.exe create 80.sys binPath=C:\\windows\\temp\\80.sys type=kernel && sc.exe start 80.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 80.sys binPath=C:\\\\windows\\\\temp\\\\80.sys type=kernel && sc.exe start 80.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 80.sys"

# 80.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068