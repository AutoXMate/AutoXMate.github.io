---
id: windows-kernel-dellinstrumentation
namespace: windows:kernel:dellinstrumentation
name: dellinstrumentation.sys
description: Elevate privileges
author: Dor00tkit
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
  template: sc.exe create dellinstrumentation.sys binPath=C:\windows\temp\dellinstrumentation.sys
    type=kernel && sc.exe start dellinstrumentation.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dellinstrumentation.sys kernel driver
  commands:
  - sc.exe create dellinstrumentation.sys binPath=C:\windows\temp\dellinstrumentation.sys
    type=kernel && sc.exe start dellinstrumentation.sys
references:
- label: Reference
  url: https://dor00tkit.github.io/Dor00tkit/posts/from-admin-to-kernel-one-year-one-driver-zero-attention/
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dellinstrumentation.sys binPath=C:\\\\windows\\\\temp\\\\dellinstrumentation.sys type=kernel && sc.exe start dellinstrumentation.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dellinstrumentation.sys"

# dellinstrumentation.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
