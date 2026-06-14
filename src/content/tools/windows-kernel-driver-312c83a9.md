---
id: windows-kernel-driver-312c83a9
namespace: windows:kernel:driver-312c83a9
name: "driver_312c83a9.sys"
description: "Sophos, from time to time, has observed a threat actor deploy variants of Poortry on different machines within a single estate during an attack. These variants contain the same payload, but signed with a different certificate than the driver first seen used during the attack."
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: "sc.exe create driver_bfcbc010.sys binPath=C:\\windows\\temp\\driver_bfcbc010.sys type=kernel && sc.exe start driver_bfcbc010.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load driver_312c83a9.sys kernel driver"
    commands:
      - "sc.exe create driver_bfcbc010.sys binPath=C:\\windows\\temp\\driver_bfcbc010.sys type=kernel && sc.exe start driver_bfcbc010.sys"
references:
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2024/08/27/burnt-cigar-2/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create driver_bfcbc010.sys binPath=C:\\\\windows\\\\temp\\\\driver_bfcbc010.sys type=kernel && sc.exe start driver_bfcbc010.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver driver_312c83a9.sys"

# driver_312c83a9.sys

Sophos, from time to time, has observed a threat actor deploy variants of Poortry on different machines within a single estate during an attack. These variants contain the same payload, but signed with a different certificate than the driver first seen used during the attack.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068