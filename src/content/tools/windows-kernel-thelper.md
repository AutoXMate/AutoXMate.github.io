---
id: windows-kernel-thelper
namespace: windows:kernel:thelper
name: "thelper.sys"
description: "OCular THelper driver with arbitrary kernel memory read/write and process manipulation capabilities. Identified in ESET EDR killers research (March 2026) with 46 execution parents linked to AgentStp campaigns abusing the driver to disable EDR products."
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
  template: "sc.exe create thelper.sys binPath=C:\\windows\\temp\\thelper.sys type=kernel && sc.exe start thelper.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load thelper.sys kernel driver"
    commands:
      - "sc.exe create thelper.sys binPath=C:\\windows\\temp\\thelper.sys type=kernel && sc.exe start thelper.sys"
references:
  - label: "Reference"
    url: "https://www.welivesecurity.com/en/eset-research/edr-killers-explained/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create thelper.sys binPath=C:\\\\windows\\\\temp\\\\thelper.sys type=kernel && sc.exe start thelper.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver thelper.sys"

# thelper.sys

OCular THelper driver with arbitrary kernel memory read/write and process manipulation capabilities. Identified in ESET EDR killers research (March 2026) with 46 execution parents linked to AgentStp campaigns abusing the driver to disable EDR products.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068