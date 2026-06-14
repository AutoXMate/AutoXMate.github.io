---
id: windows-kernel-controlcenter
namespace: windows:kernel:controlcenter
name: "ControlCenter.sys"
description: "ControlCenter.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create ControlCenter binPath=C:\\windows\\temp\\ControlCenter.sys type=kernel && sc.exe start ControlCenter"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ControlCenter.sys kernel driver"
    commands:
      - "sc.exe create ControlCenter binPath=C:\\windows\\temp\\ControlCenter.sys type=kernel && sc.exe start ControlCenter"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ControlCenter binPath=C:\\\\windows\\\\temp\\\\ControlCenter.sys type=kernel && sc.exe start ControlCenter"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ControlCenter.sys"

# ControlCenter.sys

ControlCenter.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068