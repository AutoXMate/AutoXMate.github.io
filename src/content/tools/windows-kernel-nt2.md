---
id: windows-kernel-nt2
namespace: windows:kernel:nt2
name: "nt2.sys"
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
  template: "sc.exe create nt2.sys binPath=C:\\windows\\temp \\n \\n \\n  t2.sys type=kernel && sc.exe start nt2.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nt2.sys kernel driver"
    commands:
      - "sc.exe create nt2.sys binPath=C:\\windows\\temp \\n \\n \\n  t2.sys type=kernel && sc.exe start nt2.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nt2.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  t2.sys type=kernel && sc.exe start nt2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nt2.sys"

# nt2.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068