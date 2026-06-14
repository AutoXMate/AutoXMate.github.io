---
id: windows-kernel-winio64c
namespace: windows:kernel:winio64c
name: "WinIo64C.sys"
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
  template: "sc.exe create WinIo64C.sys binPath=C:\\windows\\temp\\WinIo64C.sys type=kernel && sc.exe start WinIo64C.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load WinIo64C.sys kernel driver"
    commands:
      - "sc.exe create WinIo64C.sys binPath=C:\\windows\\temp\\WinIo64C.sys type=kernel && sc.exe start WinIo64C.sys"
references:
  - label: "Reference"
    url: " https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIo64C.sys binPath=C:\\\\windows\\\\temp\\\\WinIo64C.sys type=kernel && sc.exe start WinIo64C.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIo64C.sys"

# WinIo64C.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068