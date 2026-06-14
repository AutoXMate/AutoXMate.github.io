---
id: windows-kernel-bdapiutil64
namespace: windows:kernel:bdapiutil64
name: "BdApiUtil64.sys"
description: "Driver can be used to load unsigned drivers"
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
  template: "sc.exe create BdApiUtil64.sys binPath=C:\\windows\\temp\\BdApiUtil64.sys type=kernel && sc.exe start BdApiUtil64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load BdApiUtil64.sys kernel driver"
    commands:
      - "sc.exe create BdApiUtil64.sys binPath=C:\\windows\\temp\\BdApiUtil64.sys type=kernel && sc.exe start BdApiUtil64.sys"
references:
  - label: "Reference"
    url: "https://github.com/BlackSnufkin/BYOVD"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BdApiUtil64.sys binPath=C:\\\\windows\\\\temp\\\\BdApiUtil64.sys type=kernel && sc.exe start BdApiUtil64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BdApiUtil64.sys"

# BdApiUtil64.sys

Driver can be used to load unsigned drivers

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068