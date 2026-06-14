---
id: windows-kernel-semav6msr
namespace: windows:kernel:semav6msr
name: "semav6msr.sys"
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
  template: "sc.exe create semav6msr.sys binPath=C:\\windows\\temp\\semav6msr.sys type=kernel && sc.exe start semav6msr.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load semav6msr.sys kernel driver"
    commands:
      - "sc.exe create semav6msr.sys binPath=C:\\windows\\temp\\semav6msr.sys type=kernel && sc.exe start semav6msr.sys"
references:
  - label: "Reference"
    url: "https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md"
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create semav6msr.sys binPath=C:\\\\windows\\\\temp\\\\semav6msr.sys type=kernel && sc.exe start semav6msr.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver semav6msr.sys"

# semav6msr.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068