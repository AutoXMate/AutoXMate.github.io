---
id: windows-kernel-kbdcap64
namespace: windows:kernel:kbdcap64
name: "kbdcap64.sys"
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
trust_level: verified
execution:
  template: "sc.exe create kbdcap64.sys binPath=C:\\windows\\temp\\kbdcap64.sys type=kernel && sc.exe start kbdcap64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load kbdcap64.sys kernel driver"
    commands:
      - "sc.exe create kbdcap64.sys binPath=C:\\windows\\temp\\kbdcap64.sys type=kernel && sc.exe start kbdcap64.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create kbdcap64.sys binPath=C:\\\\windows\\\\temp\\\\kbdcap64.sys type=kernel && sc.exe start kbdcap64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver kbdcap64.sys"

# kbdcap64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068