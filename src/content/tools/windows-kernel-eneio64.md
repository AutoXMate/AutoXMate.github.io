---
id: windows-kernel-eneio64
namespace: windows:kernel:eneio64
name: "EneIo64.sys"
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
  template: "sc.exe create EneIo64.sys binPath=C:\\windows\\temp\\EneIo64.sys type=kernel && sc.exe start EneIo64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load EneIo64.sys kernel driver"
    commands:
      - "sc.exe create EneIo64.sys binPath=C:\\windows\\temp\\EneIo64.sys type=kernel && sc.exe start EneIo64.sys"
references:
  - label: "Reference"
    url: "https://gist.github.com/k4nfr3/af970e7facb09195e56f2112e1c9549c"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create EneIo64.sys binPath=C:\\\\windows\\\\temp\\\\EneIo64.sys type=kernel && sc.exe start EneIo64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver EneIo64.sys"

# EneIo64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068