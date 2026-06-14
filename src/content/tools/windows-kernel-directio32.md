---
id: windows-kernel-directio32
namespace: windows:kernel:directio32
name: DirectIo32.sys
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
  template: sc.exe create DirectIo32.sys binPath=C:\windows\temp\DirectIo32.sys type=kernel
    && sc.exe start DirectIo32.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load DirectIo32.sys kernel driver
  commands:
  - sc.exe create DirectIo32.sys binPath=C:\windows\temp\DirectIo32.sys type=kernel
    && sc.exe start DirectIo32.sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create DirectIo32.sys binPath=C:\\\\windows\\\\temp\\\\DirectIo32.sys type=kernel && sc.exe start DirectIo32.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver DirectIo32.sys"

# DirectIo32.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
