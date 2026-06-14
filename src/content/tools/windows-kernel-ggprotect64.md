---
id: windows-kernel-ggprotect64
namespace: windows:kernel:ggprotect64
name: "GGProtect64.sys"
description: "GGProtect64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create GGProtect64 binPath=C:\\windows\\temp\\GGProtect64.sys type=kernel && sc.exe start GGProtect64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load GGProtect64.sys kernel driver"
    commands:
      - "sc.exe create GGProtect64 binPath=C:\\windows\\temp\\GGProtect64.sys type=kernel && sc.exe start GGProtect64"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create GGProtect64 binPath=C:\\\\windows\\\\temp\\\\GGProtect64.sys type=kernel && sc.exe start GGProtect64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver GGProtect64.sys"

# GGProtect64.sys

GGProtect64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068