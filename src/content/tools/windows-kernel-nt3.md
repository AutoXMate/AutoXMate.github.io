---
id: windows-kernel-nt3
namespace: windows:kernel:nt3
name: "nt3.sys"
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
  template: "sc.exe create nt3.sys binPath=C:\\windows\\temp \\n \\n \\n  t3.sys type=kernel && sc.exe start nt3.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nt3.sys kernel driver"
    commands:
      - "sc.exe create nt3.sys binPath=C:\\windows\\temp \\n \\n \\n  t3.sys type=kernel && sc.exe start nt3.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nt3.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  t3.sys type=kernel && sc.exe start nt3.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nt3.sys"

# nt3.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068