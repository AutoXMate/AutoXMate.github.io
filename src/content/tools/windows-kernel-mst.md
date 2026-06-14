---
id: windows-kernel-mst
namespace: windows:kernel:mst
name: mst.sys
description: mst.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
  repository. The driver exposes dangerous kernel primitives to usermode.
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
  template: sc.exe create mst binPath=C:\windows\temp\mst.sys type=kernel && sc.exe
    start mst
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load mst.sys kernel driver
  commands:
  - sc.exe create mst binPath=C:\windows\temp\mst.sys type=kernel && sc.exe start
    mst
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mst binPath=C:\\\\windows\\\\temp\\\\mst.sys type=kernel && sc.exe start mst"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver mst.sys"

# mst.sys

mst.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
