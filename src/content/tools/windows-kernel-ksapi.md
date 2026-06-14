---
id: windows-kernel-ksapi
namespace: windows:kernel:ksapi
name: ksapi.sys
description: Driver can be used to load unsigned drivers
author: Michael Haag
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
  template: sc.exe create ksapi.sys binPath=C:\windows\temp\ksapi.sys type=kernel
    && sc.exe start ksapi.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ksapi.sys kernel driver
  commands:
  - sc.exe create ksapi.sys binPath=C:\windows\temp\ksapi.sys type=kernel && sc.exe
    start ksapi.sys
references:
- label: Reference
  url: https://github.com/BlackSnufkin/BYOVD
features:
- pipes-stdin
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ksapi.sys binPath=C:\\\\windows\\\\temp\\\\ksapi.sys type=kernel && sc.exe start ksapi.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ksapi.sys"

# ksapi.sys

Driver can be used to load unsigned drivers

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
