---
id: windows-kernel-mhyprot3
namespace: windows:kernel:mhyprot3
name: "mhyprot3.sys"
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
  template: "sc.exe create mhyprot3.sys binPath=C:\\windows\\temp\\mhyprot3.sys type=kernel && sc.exe start mhyprot3.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load mhyprot3.sys kernel driver"
    commands:
      - "sc.exe create mhyprot3.sys binPath=C:\\windows\\temp\\mhyprot3.sys type=kernel && sc.exe start mhyprot3.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mhyprot3.sys binPath=C:\\\\windows\\\\temp\\\\mhyprot3.sys type=kernel && sc.exe start mhyprot3.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver mhyprot3.sys"

# mhyprot3.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068