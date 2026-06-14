---
id: windows-kernel-nt5
namespace: windows:kernel:nt5
name: "nt5.sys"
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
  template: "sc.exe create nt5.sys binPath=C:\\windows\\temp \\n \\n \\n  t5.sys type=kernel && sc.exe start nt5.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nt5.sys kernel driver"
    commands:
      - "sc.exe create nt5.sys binPath=C:\\windows\\temp \\n \\n \\n  t5.sys type=kernel && sc.exe start nt5.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nt5.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  t5.sys type=kernel && sc.exe start nt5.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nt5.sys"

# nt5.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068