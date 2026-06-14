---
id: windows-kernel-ene
namespace: windows:kernel:ene
name: ene.sys
description: Elevate privileges
author: Nasreddine Bencherchali
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create ene.sys binPath=C:\windows\temp\ene.sys type=kernel && sc.exe
    start ene.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ene.sys kernel driver
  commands:
  - sc.exe create ene.sys binPath=C:\windows\temp\ene.sys type=kernel && sc.exe start
    ene.sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ene.sys binPath=C:\\\\windows\\\\temp\\\\ene.sys type=kernel && sc.exe start ene.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ene.sys"

# ene.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
