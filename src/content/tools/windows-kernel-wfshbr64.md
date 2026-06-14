---
id: windows-kernel-wfshbr64
namespace: windows:kernel:wfshbr64
name: "wfshbr64.sys"
description: "wfshbr64.sys and wfshbr32.sys specially crafted payload allows arbitrary user to perform bitwise operation with arbitrary EPROCESS offset and flags value to purposely elevate the game process to CodeGen Full protection by manipulating EPROCESS.Protection and EPROCESS.SignatureLevel flags (security hole as a feature).

The driver is signed by Microsoft hardware compatibility publisher that is submitted via Microsoft Hardware Program."
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
  template: "sc.exe create wfshbr64.sys binPath=C:\\windows\\temp\\wfshbr64.sys type=kernel && sc.exe start wfshbr64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load wfshbr64.sys kernel driver"
    commands:
      - "sc.exe create wfshbr64.sys binPath=C:\\windows\\temp\\wfshbr64.sys type=kernel && sc.exe start wfshbr64.sys"
references:
  - label: "Reference"
    url: "https://github.com/kkent030315/CVE-2022-42046"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create wfshbr64.sys binPath=C:\\\\windows\\\\temp\\\\wfshbr64.sys type=kernel && sc.exe start wfshbr64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wfshbr64.sys"

# wfshbr64.sys

wfshbr64.sys and wfshbr32.sys specially crafted payload allows arbitrary user to perform bitwise operation with arbitrary EPROCESS offset and flags value to purposely elevate the game process to CodeGen Full protection by manipulating EPROCESS.Protection and EPROCESS.SignatureLevel flags (security hole as a feature).

The driver is signed by Microsoft hardware compatibility publisher that is submitted via Microsoft Hardware Program.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068