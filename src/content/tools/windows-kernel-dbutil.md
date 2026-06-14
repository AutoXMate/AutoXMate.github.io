---
id: windows-kernel-dbutil
namespace: windows:kernel:dbutil
name: dbutil.sys
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
  template: sc.exe create dbutil.sys binPath=C:\windows\temp\dbutil.sys type=kernel
    && sc.exe start dbutil.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dbutil.sys kernel driver
  commands:
  - sc.exe create dbutil.sys binPath=C:\windows\temp\dbutil.sys type=kernel && sc.exe
    start dbutil.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dbutil.sys binPath=C:\\\\windows\\\\temp\\\\dbutil.sys type=kernel && sc.exe start dbutil.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dbutil.sys"

# dbutil.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
