---
id: windows-kernel-magdrvamd64
namespace: windows:kernel:magdrvamd64
name: "magdrvamd64.sys"
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
  template: "sc.exe create magdrvamd64.sys binPath=C:\\windows\\temp\\magdrvamd64.sys     type=kernel && sc.exe start magdrvamd64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load magdrvamd64.sys kernel driver"
    commands:
      - "sc.exe create magdrvamd64.sys binPath=C:\\windows\\temp\\magdrvamd64.sys     type=kernel && sc.exe start magdrvamd64.sys"
references:
  - label: "Reference"
    url: "https://www.unknowncheats.me/forum/anti-cheat-bypass/334557-vulnerable-driver-megathread.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create magdrvamd64.sys binPath=C:\\\\windows\\\\temp\\\\magdrvamd64.sys     type=kernel && sc.exe start magdrvamd64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver magdrvamd64.sys"

# magdrvamd64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068