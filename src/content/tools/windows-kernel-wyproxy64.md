---
id: windows-kernel-wyproxy64
namespace: windows:kernel:wyproxy64
name: "WYProxy64.sys"
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
  template: "sc.exe create WYProxy64.sys binPath=C:\\windows\\temp\\WYProxy64.sys type=kernel && sc.exe start WYProxy64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load WYProxy64.sys kernel driver"
    commands:
      - "sc.exe create WYProxy64.sys binPath=C:\\windows\\temp\\WYProxy64.sys type=kernel && sc.exe start WYProxy64.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WYProxy64.sys binPath=C:\\\\windows\\\\temp\\\\WYProxy64.sys type=kernel && sc.exe start WYProxy64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WYProxy64.sys"

# WYProxy64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068