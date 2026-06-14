---
id: windows-kernel-7
namespace: windows:kernel:7
name: "7.sys"
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
  template: "sc.exe create 7.sys binPath=C:\\windows\\temp\\7.sys type=kernel && sc.exe start 7.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load 7.sys kernel driver"
    commands:
      - "sc.exe create 7.sys binPath=C:\\windows\\temp\\7.sys type=kernel && sc.exe start 7.sys"
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 7.sys binPath=C:\\\\windows\\\\temp\\\\7.sys type=kernel && sc.exe start 7.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 7.sys"

# 7.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068