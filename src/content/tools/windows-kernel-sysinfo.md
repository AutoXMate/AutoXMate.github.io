---
id: windows-kernel-sysinfo
namespace: windows:kernel:sysinfo
name: "SysInfo.sys"
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
  template: "sc.exe create SysInfo.sys binPath=C:\\windows\\temp\\SysInfo.sys type=kernel && sc.exe start SysInfo.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load SysInfo.sys kernel driver"
    commands:
      - "sc.exe create SysInfo.sys binPath=C:\\windows\\temp\\SysInfo.sys type=kernel && sc.exe start SysInfo.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SysInfo.sys binPath=C:\\\\windows\\\\temp\\\\SysInfo.sys type=kernel && sc.exe start SysInfo.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SysInfo.sys"

# SysInfo.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068