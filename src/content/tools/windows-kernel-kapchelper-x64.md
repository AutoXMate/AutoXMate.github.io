---
id: windows-kernel-kapchelper-x64
namespace: windows:kernel:kapchelper-x64
name: KApcHelper_x64.sys
description: Vulnerable driving using the stolen Nvidia Certificate.
author: Guus Verbeek
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
  template: sc.exe create KApcHelper_x64.sys binPath=C:\windows\temp\KApcHelper_x64.sys
    type=kernel && sc.exe start KApcHelper_x64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load KApcHelper_x64.sys kernel driver
  commands:
  - sc.exe create KApcHelper_x64.sys binPath=C:\windows\temp\KApcHelper_x64.sys type=kernel
    && sc.exe start KApcHelper_x64.sys
references:
- label: Reference
  url: https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware
features:
- encryption
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create KApcHelper_x64.sys binPath=C:\\\\windows\\\\temp\\\\KApcHelper_x64.sys type=kernel && sc.exe start KApcHelper_x64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver KApcHelper_x64.sys"

# KApcHelper_x64.sys

Vulnerable driving using the stolen Nvidia Certificate.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
