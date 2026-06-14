---
id: windows-kernel-gameink
namespace: windows:kernel:gameink
name: "gameink.sys"
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
  template: "sc.exe create gameink.sys binPath=C:\\windows\\temp\\gameink.sys type=kernel && sc.exe start gameink.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load gameink.sys kernel driver"
    commands:
      - "sc.exe create gameink.sys binPath=C:\\windows\\temp\\gameink.sys type=kernel && sc.exe start gameink.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create gameink.sys binPath=C:\\\\windows\\\\temp\\\\gameink.sys type=kernel && sc.exe start gameink.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver gameink.sys"

# gameink.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068