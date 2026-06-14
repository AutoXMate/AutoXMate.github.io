---
id: windows-kernel-sysinfox64
namespace: windows:kernel:sysinfox64
name: "SysInfoX64.sys"
description: "SysInfoX64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
author: "Michael Haag"
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
  template: "sc.exe create SysInfoX64 binPath=C:\\windows\\temp\\SysInfoX64.sys type=kernel && sc.exe start SysInfoX64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load SysInfoX64.sys kernel driver"
    commands:
      - "sc.exe create SysInfoX64 binPath=C:\\windows\\temp\\SysInfoX64.sys type=kernel && sc.exe start SysInfoX64"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SysInfoX64 binPath=C:\\\\windows\\\\temp\\\\SysInfoX64.sys type=kernel && sc.exe start SysInfoX64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SysInfoX64.sys"

# SysInfoX64.sys

SysInfoX64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068