---
id: windows-kernel-capcom
namespace: windows:kernel:capcom
name: "capcom.sys"
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
  template: "sc.exe create capcom.sys binPath=C:\\windows\\temp\\capcom.sys type=kernel && sc.exe start capcom.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load capcom.sys kernel driver"
    commands:
      - "sc.exe create capcom.sys binPath=C:\\windows\\temp\\capcom.sys type=kernel && sc.exe start capcom.sys"
references:
  - label: "Reference"
    url: "https://github.com/elastic/protections-artifacts/search?q=VulnDriver"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create capcom.sys binPath=C:\\\\windows\\\\temp\\\\capcom.sys type=kernel && sc.exe start capcom.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver capcom.sys"

# capcom.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068