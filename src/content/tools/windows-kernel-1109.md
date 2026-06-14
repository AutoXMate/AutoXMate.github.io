---
id: windows-kernel-1109
namespace: windows:kernel:1109
name: "1109.sys"
description: "1109.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create 1109 binPath=C:\\windows\\temp\\1109.sys type=kernel && sc.exe start 1109"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load 1109.sys kernel driver"
    commands:
      - "sc.exe create 1109 binPath=C:\\windows\\temp\\1109.sys type=kernel && sc.exe start 1109"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 1109 binPath=C:\\\\windows\\\\temp\\\\1109.sys type=kernel && sc.exe start 1109"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 1109.sys"

# 1109.sys

1109.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068