---
id: windows-kernel-msr
namespace: windows:kernel:msr
name: msr.sys
description: 'Identified on the MSFT Driver Block list, non-admin can write MSR. '
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create msr.sys binPath=C:\windows\temp\msr.sys type=kernel && sc.exe
    start msr.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load msr.sys kernel driver
  commands:
  - sc.exe create msr.sys binPath=C:\windows\temp\msr.sys type=kernel && sc.exe start
    msr.sys
references:
- label: Reference
  url: https://twitter.com/wdormann/status/1699878227261411699
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/microsoft-recommended-driver-block-rules
features:
- file-system
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create msr.sys binPath=C:\\\\windows\\\\temp\\\\msr.sys type=kernel && sc.exe start msr.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver msr.sys"

# msr.sys

Identified on the MSFT Driver Block list, non-admin can write MSR. 

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
