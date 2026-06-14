---
id: windows-kernel-nqrmq
namespace: windows:kernel:nqrmq
name: NQrmq.sys
description: Found via RichPEHeaderHash pivoting.
author: Michael Haag
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
  template: sc.exe create NQrmq.sys binPath=C:\windows\temp\NQrmq.sys type=kernel
    && sc.exe start NQrmq.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load NQrmq.sys kernel driver
  commands:
  - sc.exe create NQrmq.sys binPath=C:\windows\temp\NQrmq.sys type=kernel && sc.exe
    start NQrmq.sys
features:
- file-system
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NQrmq.sys binPath=C:\\\\windows\\\\temp\\\\NQrmq.sys type=kernel && sc.exe start NQrmq.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NQrmq.sys"

# NQrmq.sys

Found via RichPEHeaderHash pivoting.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
