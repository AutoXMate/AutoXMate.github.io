---
id: windows-kernel-dcr
namespace: windows:kernel:dcr
name: "dcr.sys"
description: "DriveCrypt Dcr.sys vulnerability exploit for bypassing x64 DSE"
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
  template: "sc.exe create dcr.sys binPath=C:\\windows\\temp\\dcr.sys type=kernel && sc.exe start dcr.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load dcr.sys kernel driver"
    commands:
      - "sc.exe create dcr.sys binPath=C:\\windows\\temp\\dcr.sys type=kernel && sc.exe start dcr.sys"
references:
  - label: "Reference"
    url: "https://github.com/wjcsharp/DriveCrypt"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dcr.sys binPath=C:\\\\windows\\\\temp\\\\dcr.sys type=kernel && sc.exe start dcr.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dcr.sys"

# dcr.sys

DriveCrypt Dcr.sys vulnerability exploit for bypassing x64 DSE

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068