---
id: windows-kernel-2
namespace: windows:kernel:2
name: "2.sys"
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
  template: "sc.exe create 2.sys binPath=C:\\windows\\temp\\2.sys type=kernel && sc.exe start 2.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load 2.sys kernel driver"
    commands:
      - "sc.exe create 2.sys binPath=C:\\windows\\temp\\2.sys type=kernel && sc.exe start 2.sys"
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 2.sys binPath=C:\\\\windows\\\\temp\\\\2.sys type=kernel && sc.exe start 2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 2.sys"

# 2.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants