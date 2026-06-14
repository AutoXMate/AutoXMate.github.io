---
id: windows-kernel-winio64a
namespace: windows:kernel:winio64a
name: WinIo64A.sys
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
  template: sc.exe create WinIo64A.sys binPath=C:\windows\temp\WinIo64A.sys type=kernel
    && sc.exe start WinIo64A.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinIo64A.sys kernel driver
  commands:
  - sc.exe create WinIo64A.sys binPath=C:\windows\temp\WinIo64A.sys type=kernel &&
    sc.exe start WinIo64A.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIo64A.sys binPath=C:\\\\windows\\\\temp\\\\WinIo64A.sys type=kernel && sc.exe start WinIo64A.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIo64A.sys"

# WinIo64A.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
