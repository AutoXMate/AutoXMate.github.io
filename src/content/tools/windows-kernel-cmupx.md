---
id: windows-kernel-cmupx
namespace: windows:kernel:cmupx
name: "CmUpx.sys"
description: "CmUpx.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create CmUpx binPath=C:\\windows\\temp\\CmUpx.sys type=kernel && sc.exe start CmUpx"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load CmUpx.sys kernel driver"
    commands:
      - "sc.exe create CmUpx binPath=C:\\windows\\temp\\CmUpx.sys type=kernel && sc.exe start CmUpx"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CmUpx binPath=C:\\\\windows\\\\temp\\\\CmUpx.sys type=kernel && sc.exe start CmUpx"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CmUpx.sys"

# CmUpx.sys

CmUpx.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068