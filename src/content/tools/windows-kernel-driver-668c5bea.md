---
id: windows-kernel-driver-668c5bea
namespace: windows:kernel:driver-668c5bea
name: driver_668c5bea.sys
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
  template: sc.exe create driver_fdd16a94.sys binPath=C:\windows\temp\driver_fdd16a94.sys
    type=kernel && sc.exe start driver_fdd16a94.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load driver_668c5bea.sys kernel driver
  commands:
  - sc.exe create driver_fdd16a94.sys binPath=C:\windows\temp\driver_fdd16a94.sys
    type=kernel && sc.exe start driver_fdd16a94.sys
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
    command: "sc.exe create driver_fdd16a94.sys binPath=C:\\\\windows\\\\temp\\\\driver_fdd16a94.sys type=kernel && sc.exe start driver_fdd16a94.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver driver_668c5bea.sys"

# driver_668c5bea.sys

Sophos, from time to time, has observed a threat actor deploy variants of Poortry on different machines within a single estate during an attack. These variants contain the same payload, but signed with a different certificate than the driver first seen used during the attack.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
