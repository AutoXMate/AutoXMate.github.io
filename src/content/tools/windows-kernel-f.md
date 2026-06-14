---
id: windows-kernel-f
namespace: windows:kernel:f
name: f.sys
description: Sophos, from time to time, has observed a threat actor deploy variants
  of Poortry on different machines within a single estate during an attack. These
  variants contain the same payload, but signed with a different certificate than
  the driver first seen used during the attack.
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: sc.exe create f.sys binPath=C:\windows\temp\f.sys type=kernel && sc.exe
    start f.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load f.sys kernel driver
  commands:
  - sc.exe create f.sys binPath=C:\windows\temp\f.sys type=kernel && sc.exe start
    f.sys
references:
- label: Reference
  url: https://news.sophos.com/en-us/2024/08/27/burnt-cigar-2/
features:
- encryption
- pipes-stdin
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create f.sys binPath=C:\\\\windows\\\\temp\\\\f.sys type=kernel && sc.exe start f.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver f.sys"

# f.sys

Sophos, from time to time, has observed a threat actor deploy variants
    of Poortry on different machines within a single estate during an attack. These
    variants contain the same payload, but signed with a different certificate than
    the driver first seen used during the attack.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
