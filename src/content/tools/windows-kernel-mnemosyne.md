---
id: windows-kernel-mnemosyne
namespace: windows:kernel:mnemosyne
name: "Mnemosyne.sys"
description: "Mnemosyne.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create Mnemosyne binPath=C:\\windows\\temp\\Mnemosyne.sys type=kernel && sc.exe start Mnemosyne"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load Mnemosyne.sys kernel driver"
    commands:
      - "sc.exe create Mnemosyne binPath=C:\\windows\\temp\\Mnemosyne.sys type=kernel && sc.exe start Mnemosyne"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Mnemosyne binPath=C:\\\\windows\\\\temp\\\\Mnemosyne.sys type=kernel && sc.exe start Mnemosyne"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Mnemosyne.sys"

# Mnemosyne.sys

Mnemosyne.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068