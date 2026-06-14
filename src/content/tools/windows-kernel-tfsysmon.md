---
id: windows-kernel-tfsysmon
namespace: windows:kernel:tfsysmon
name: "TfSysMon.sys"
description: "Elevate privileges"
author: "rahulwt"
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
  template: "sc.exe create TfSysMon.sys binPath=C:\\windows\\temp\\TfSysMon.sys type=kernel && sc.exe start TfSysMon.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load TfSysMon.sys kernel driver"
    commands:
      - "sc.exe create TfSysMon.sys binPath=C:\\windows\\temp\\TfSysMon.sys type=kernel && sc.exe start TfSysMon.sys"
references:
  - label: "Reference"
    url: "https://github.com/BlackSnufkin/BYOVD/tree/main/TfSysMon-Killer"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TfSysMon.sys binPath=C:\\\\windows\\\\temp\\\\TfSysMon.sys type=kernel && sc.exe start TfSysMon.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TfSysMon.sys"

# TfSysMon.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068