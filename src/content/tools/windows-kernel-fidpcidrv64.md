---
id: windows-kernel-fidpcidrv64
namespace: windows:kernel:fidpcidrv64
name: "fidpcidrv64.sys"
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
  template: "sc.exe create fidpcidrv64.sys binPath=C:\\windows\\temp\\fidpcidrv64.sys     type=kernel && sc.exe start fidpcidrv64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load fidpcidrv64.sys kernel driver"
    commands:
      - "sc.exe create fidpcidrv64.sys binPath=C:\\windows\\temp\\fidpcidrv64.sys     type=kernel && sc.exe start fidpcidrv64.sys"
references:
  - label: "Reference"
    url: "https://github.com/elastic/protections-artifacts/search?q=VulnDriver"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create fidpcidrv64.sys binPath=C:\\\\windows\\\\temp\\\\fidpcidrv64.sys     type=kernel && sc.exe start fidpcidrv64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver fidpcidrv64.sys"

# fidpcidrv64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068