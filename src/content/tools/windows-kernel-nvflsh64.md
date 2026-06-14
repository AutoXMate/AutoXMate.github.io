---
id: windows-kernel-nvflsh64
namespace: windows:kernel:nvflsh64
name: "nvflsh64.sys"
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
  template: "sc.exe create nvflsh64.sys binPath=C:\\windows\\temp \\n \\n \\n  vflsh64.sys type=kernel && sc.exe start nvflsh64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nvflsh64.sys kernel driver"
    commands:
      - "sc.exe create nvflsh64.sys binPath=C:\\windows\\temp \\n \\n \\n  vflsh64.sys type=kernel && sc.exe start nvflsh64.sys"
references:
  - label: "Reference"
    url: "https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nvflsh64.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  vflsh64.sys type=kernel && sc.exe start nvflsh64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nvflsh64.sys"

# nvflsh64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068