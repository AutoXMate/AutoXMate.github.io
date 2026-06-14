---
id: windows-kernel-msrhook
namespace: windows:kernel:msrhook
name: "msrhook.sys"
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
  template: "sc.exe create msrhook.sys binPath=C:\\windows\\temp\\msrhook.sys type=kernel && sc.exe start msrhook.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load msrhook.sys kernel driver"
    commands:
      - "sc.exe create msrhook.sys binPath=C:\\windows\\temp\\msrhook.sys type=kernel && sc.exe start msrhook.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create msrhook.sys binPath=C:\\\\windows\\\\temp\\\\msrhook.sys type=kernel && sc.exe start msrhook.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver msrhook.sys"

# msrhook.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068