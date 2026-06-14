---
id: windows-kernel-6c8a
namespace: windows:kernel:6c8a
name: "6c8a.sys"
description: "6c8a.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create 6c8a binPath=C:\\windows\\temp\\6c8a.sys type=kernel && sc.exe start 6c8a"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load 6c8a.sys kernel driver"
    commands:
      - "sc.exe create 6c8a binPath=C:\\windows\\temp\\6c8a.sys type=kernel && sc.exe start 6c8a"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create 6c8a binPath=C:\\\\windows\\\\temp\\\\6c8a.sys type=kernel && sc.exe start 6c8a"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver 6c8a.sys"

# 6c8a.sys

6c8a.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068