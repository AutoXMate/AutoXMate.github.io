---
id: windows-kernel-termdd
namespace: windows:kernel:termdd
name: "termdd.sys"
description: "A vulnerable kernel driver that can be used to disable Code Integrity"
author: "Andrea Monzani, Antonio Parata"
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
  template: "sc.exe create termdd.sys binPath=C:\\windows\\temp\\termdd.sys type=kernel && sc.exe start termdd.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load termdd.sys kernel driver"
    commands:
      - "sc.exe create termdd.sys binPath=C:\\windows\\temp\\termdd.sys type=kernel && sc.exe start termdd.sys"
references:
  - label: "Reference"
    url: "https://kat.lua.cz/posts/Some_fun_with_vintage_bugs_and_driver_signing_enforcement/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create termdd.sys binPath=C:\\\\windows\\\\temp\\\\termdd.sys type=kernel && sc.exe start termdd.sys"

# termdd.sys

A vulnerable kernel driver that can be used to disable Code Integrity

**Use Case:** Code Integrity Tampering

**Required Privileges:** Admin privileges

**MITRE ATT&CK:** T1068