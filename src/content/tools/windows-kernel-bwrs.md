---
id: windows-kernel-bwrs
namespace: windows:kernel:bwrs
name: bwrs.sys
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
  template: sc.exe create bwrs.sys binPath=C:\windows\temp\bwrs.sys type=kernel &&
    sc.exe start bwrs.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load bwrs.sys kernel driver
  commands:
  - sc.exe create bwrs.sys binPath=C:\windows\temp\bwrs.sys type=kernel && sc.exe
    start bwrs.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create bwrs.sys binPath=C:\\\\windows\\\\temp\\\\bwrs.sys type=kernel && sc.exe start bwrs.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver bwrs.sys"

# bwrs.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
