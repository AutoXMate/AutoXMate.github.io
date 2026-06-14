---
id: windows-kernel-lurker
namespace: windows:kernel:lurker
name: "Lurker.sys"
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
  template: "sc.exe create Lurker.sys binPath=C:\\windows\\temp\\Lurker.sys type=kernel && sc.exe start Lurker.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load Lurker.sys kernel driver"
    commands:
      - "sc.exe create Lurker.sys binPath=C:\\windows\\temp\\Lurker.sys type=kernel && sc.exe start Lurker.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Lurker.sys binPath=C:\\\\windows\\\\temp\\\\Lurker.sys type=kernel && sc.exe start Lurker.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Lurker.sys"

# Lurker.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068