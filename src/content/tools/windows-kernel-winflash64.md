---
id: windows-kernel-winflash64
namespace: windows:kernel:winflash64
name: "WinFlash64.sys"
description: "Elevate privileges"
author: "Nasreddine Bencherchali"
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
  template: "sc.exe create WinFlash64.sys binPath=C:\\windows\\temp\\WinFlash64.sys type=kernel && sc.exe start WinFlash64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load WinFlash64.sys kernel driver"
    commands:
      - "sc.exe create WinFlash64.sys binPath=C:\\windows\\temp\\WinFlash64.sys type=kernel && sc.exe start WinFlash64.sys"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinFlash64.sys binPath=C:\\\\windows\\\\temp\\\\WinFlash64.sys type=kernel && sc.exe start WinFlash64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinFlash64.sys"

# WinFlash64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants