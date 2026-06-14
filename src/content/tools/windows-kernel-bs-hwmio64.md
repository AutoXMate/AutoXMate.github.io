---
id: windows-kernel-bs-hwmio64
namespace: windows:kernel:bs-hwmio64
name: "BS_HWMIo64.sys"
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
  template: "sc.exe create BS_HWMIo64.sys binPath=C:\\windows\\temp\\BS_HWMIo64.sys type=kernel && sc.exe start BS_HWMIo64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load BS_HWMIo64.sys kernel driver"
    commands:
      - "sc.exe create BS_HWMIo64.sys binPath=C:\\windows\\temp\\BS_HWMIo64.sys type=kernel && sc.exe start BS_HWMIo64.sys"
references:
  - label: "Reference"
    url: "https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_HWMIo64.sys binPath=C:\\\\windows\\\\temp\\\\BS_HWMIo64.sys type=kernel && sc.exe start BS_HWMIo64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_HWMIo64.sys"

# BS_HWMIo64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068