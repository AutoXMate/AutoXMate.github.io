---
id: windows-kernel-prokiller64
namespace: windows:kernel:prokiller64
name: "prokiller64.sys"
description: "Signed POORTRY Samples"
author: "Guus Verbeek"
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
  template: "sc.exe create prokiller64.sys binPath=C:\\windows\\temp\\prokiller64.sys type=kernel && sc.exe start prokiller64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load prokiller64.sys kernel driver"
    commands:
      - "sc.exe create prokiller64.sys binPath=C:\\windows\\temp\\prokiller64.sys type=kernel && sc.exe start prokiller64.sys"
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware"
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create prokiller64.sys binPath=C:\\\\windows\\\\temp\\\\prokiller64.sys type=kernel && sc.exe start prokiller64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver prokiller64.sys"

# prokiller64.sys

Signed POORTRY Samples

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068