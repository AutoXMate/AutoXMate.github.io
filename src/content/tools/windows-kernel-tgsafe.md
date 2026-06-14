---
id: windows-kernel-tgsafe
namespace: windows:kernel:tgsafe
name: "TGSafe.sys"
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
  template: "sc.exe create TGSafe.sys binPath=C:\\windows\\temp\\TGSafe.sys type=kernel && sc.exe start TGSafe.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load TGSafe.sys kernel driver"
    commands:
      - "sc.exe create TGSafe.sys binPath=C:\\windows\\temp\\TGSafe.sys type=kernel && sc.exe start TGSafe.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TGSafe.sys binPath=C:\\\\windows\\\\temp\\\\TGSafe.sys type=kernel && sc.exe start TGSafe.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TGSafe.sys"

# TGSafe.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068