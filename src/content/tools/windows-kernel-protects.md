---
id: windows-kernel-protects
namespace: windows:kernel:protects
name: "ProtectS.sys"
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
  template: "sc.exe create ProtectS.sys binPath=C:\\windows\\temp\\ProtectS.sys type=kernel && sc.exe start ProtectS.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ProtectS.sys kernel driver"
    commands:
      - "sc.exe create ProtectS.sys binPath=C:\\windows\\temp\\ProtectS.sys type=kernel && sc.exe start ProtectS.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ProtectS.sys binPath=C:\\\\windows\\\\temp\\\\ProtectS.sys type=kernel && sc.exe start ProtectS.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ProtectS.sys"

# ProtectS.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068