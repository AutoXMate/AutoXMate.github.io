---
id: windows-kernel-enetechio64
namespace: windows:kernel:enetechio64
name: "EneTechIo64.sys"
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
  template: "sc.exe create EneTechIo64.sys binPath=C:\\windows\\temp\\EneTechIo64.sys     type=kernel && sc.exe start EneTechIo64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load EneTechIo64.sys kernel driver"
    commands:
      - "sc.exe create EneTechIo64.sys binPath=C:\\windows\\temp\\EneTechIo64.sys     type=kernel && sc.exe start EneTechIo64.sys"
references:
  - label: "Reference"
    url: "https://github.com/hfiref0x/KDU/releases/tag/v1.2.0"
  - label: "Reference"
    url: "https://gist.github.com/k4nfr3/af970e7facb09195e56f2112e1c9549c"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create EneTechIo64.sys binPath=C:\\\\windows\\\\temp\\\\EneTechIo64.sys     type=kernel && sc.exe start EneTechIo64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver EneTechIo64.sys"

# EneTechIo64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068