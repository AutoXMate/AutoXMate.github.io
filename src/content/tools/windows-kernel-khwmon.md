---
id: windows-kernel-khwmon
namespace: windows:kernel:khwmon
name: "Khwmon.sys"
description: "Khwmon.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create Khwmon binPath=C:\\windows\\temp\\Khwmon.sys type=kernel && sc.exe start Khwmon"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load Khwmon.sys kernel driver"
    commands:
      - "sc.exe create Khwmon binPath=C:\\windows\\temp\\Khwmon.sys type=kernel && sc.exe start Khwmon"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Khwmon binPath=C:\\\\windows\\\\temp\\\\Khwmon.sys type=kernel && sc.exe start Khwmon"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Khwmon.sys"

# Khwmon.sys

Khwmon.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068