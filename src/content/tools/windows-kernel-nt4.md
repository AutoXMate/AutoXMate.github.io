---
id: windows-kernel-nt4
namespace: windows:kernel:nt4
name: nt4.sys
description: Elevate privileges
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: community
execution:
  template: sc.exe create nt4.sys binPath=C:\windows\temp \n \n \n  t4.sys type=kernel
    && sc.exe start nt4.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load nt4.sys kernel driver
  commands:
  - sc.exe create nt4.sys binPath=C:\windows\temp \n \n \n  t4.sys type=kernel &&
    sc.exe start nt4.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nt4.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  t4.sys type=kernel && sc.exe start nt4.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nt4.sys"

# nt4.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
