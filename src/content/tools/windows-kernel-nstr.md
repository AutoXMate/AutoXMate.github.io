---
id: windows-kernel-nstr
namespace: windows:kernel:nstr
name: "nstr.sys"
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
  template: "sc.exe create nstr.sys binPath=C:\\windows\\temp \\n \\n \\n  str.sys type=kernel && sc.exe start nstr.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nstr.sys kernel driver"
    commands:
      - "sc.exe create nstr.sys binPath=C:\\windows\\temp \\n \\n \\n  str.sys type=kernel && sc.exe start nstr.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nstr.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  str.sys type=kernel && sc.exe start nstr.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nstr.sys"

# nstr.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068