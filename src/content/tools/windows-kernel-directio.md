---
id: windows-kernel-directio
namespace: windows:kernel:directio
name: "DirectIo.sys"
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
  template: "sc.exe create DirectIo.sys binPath=C:\\windows\\temp\\DirectIo.sys type=kernel && sc.exe start DirectIo.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load DirectIo.sys kernel driver"
    commands:
      - "sc.exe create DirectIo.sys binPath=C:\\windows\\temp\\DirectIo.sys type=kernel && sc.exe start DirectIo.sys"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create DirectIo.sys binPath=C:\\\\windows\\\\temp\\\\DirectIo.sys type=kernel && sc.exe start DirectIo.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver DirectIo.sys"

# DirectIo.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants