---
id: windows-kernel-poortry
namespace: windows:kernel:poortry
name: "POORTRY.sys"
description: "Driver categorized as POORTRY by Mandiant."
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
  template: "sc.exe create POORTRY.sys binPath=C:\\windows\\temp\\POORTRY.sys type=kernel && sc.exe start POORTRY.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load POORTRY.sys kernel driver"
    commands:
      - "sc.exe create POORTRY.sys binPath=C:\\windows\\temp\\POORTRY.sys type=kernel && sc.exe start POORTRY.sys"
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create POORTRY.sys binPath=C:\\\\windows\\\\temp\\\\POORTRY.sys type=kernel && sc.exe start POORTRY.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver POORTRY.sys"

# POORTRY.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068