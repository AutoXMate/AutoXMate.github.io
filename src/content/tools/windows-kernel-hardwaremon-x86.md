---
id: windows-kernel-hardwaremon-x86
namespace: windows:kernel:hardwaremon-x86
name: "HardwareMon-x86.sys"
description: "HardwareMon-x86.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create HardwareMon-x86 binPath=C:\\windows\\temp\\HardwareMon-x86.sys type=kernel && sc.exe start HardwareMon-x86"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load HardwareMon-x86.sys kernel driver"
    commands:
      - "sc.exe create HardwareMon-x86 binPath=C:\\windows\\temp\\HardwareMon-x86.sys type=kernel && sc.exe start HardwareMon-x86"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create HardwareMon-x86 binPath=C:\\\\windows\\\\temp\\\\HardwareMon-x86.sys type=kernel && sc.exe start HardwareMon-x86"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver HardwareMon-x86.sys"

# HardwareMon-x86.sys

HardwareMon-x86.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068