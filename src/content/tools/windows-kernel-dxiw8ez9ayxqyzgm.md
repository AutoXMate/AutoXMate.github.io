---
id: windows-kernel-dxiw8ez9ayxqyzgm
namespace: windows:kernel:dxiw8ez9ayxqyzgm
name: dXIw8eZ9aYxQYzgm.sys
description: dXIw8eZ9aYxQYzgm.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create dXIw8eZ9aYxQYzgm binPath=C:\windows\temp\dXIw8eZ9aYxQYzgm.sys
    type=kernel && sc.exe start dXIw8eZ9aYxQYzgm
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dXIw8eZ9aYxQYzgm.sys kernel driver
  commands:
  - sc.exe create dXIw8eZ9aYxQYzgm binPath=C:\windows\temp\dXIw8eZ9aYxQYzgm.sys type=kernel
    && sc.exe start dXIw8eZ9aYxQYzgm
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
    command: "sc.exe create dXIw8eZ9aYxQYzgm binPath=C:\\\\windows\\\\temp\\\\dXIw8eZ9aYxQYzgm.sys type=kernel && sc.exe start dXIw8eZ9aYxQYzgm"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dXIw8eZ9aYxQYzgm.sys"

# dXIw8eZ9aYxQYzgm.sys

dXIw8eZ9aYxQYzgm.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
