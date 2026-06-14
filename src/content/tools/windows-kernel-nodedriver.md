---
id: windows-kernel-nodedriver
namespace: windows:kernel:nodedriver
name: "NodeDriver.sys"
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
  template: "sc.exe create NodeDriver.sys binPath=C:\\windows\\temp\\NodeDriver.sys type=kernel && sc.exe start NodeDriver.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load NodeDriver.sys kernel driver"
    commands:
      - "sc.exe create NodeDriver.sys binPath=C:\\windows\\temp\\NodeDriver.sys type=kernel && sc.exe start NodeDriver.sys"
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NodeDriver.sys binPath=C:\\\\windows\\\\temp\\\\NodeDriver.sys type=kernel && sc.exe start NodeDriver.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NodeDriver.sys"

# NodeDriver.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068