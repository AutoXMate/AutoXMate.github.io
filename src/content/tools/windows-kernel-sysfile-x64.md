---
id: windows-kernel-sysfile-x64
namespace: windows:kernel:sysfile-x64
name: SysFile_X64.sys
description: SysFile_X64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
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
  template: sc.exe create SysFile_X64 binPath=C:\windows\temp\SysFile_X64.sys type=kernel
    && sc.exe start SysFile_X64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load SysFile_X64.sys kernel driver
  commands:
  - sc.exe create SysFile_X64 binPath=C:\windows\temp\SysFile_X64.sys type=kernel
    && sc.exe start SysFile_X64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- local
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SysFile_X64 binPath=C:\\\\windows\\\\temp\\\\SysFile_X64.sys type=kernel && sc.exe start SysFile_X64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SysFile_X64.sys"

# SysFile_X64.sys

SysFile_X64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
