---
id: windows-kernel-lsigetwin-sliffdriver
namespace: windows:kernel:lsigetwin-sliffdriver
name: "lsigetwin_SliffDriver.sys"
description: "lsigetwin_SliffDriver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create lsigetwin_SliffDriver binPath=C:\\windows\\temp\\lsigetwin_SliffDriver.sys type=kernel && sc.exe start lsigetwin_SliffDriver"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load lsigetwin_SliffDriver.sys kernel driver"
    commands:
      - "sc.exe create lsigetwin_SliffDriver binPath=C:\\windows\\temp\\lsigetwin_SliffDriver.sys type=kernel && sc.exe start lsigetwin_SliffDriver"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create lsigetwin_SliffDriver binPath=C:\\\\windows\\\\temp\\\\lsigetwin_SliffDriver.sys type=kernel && sc.exe start lsigetwin_SliffDriver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver lsigetwin_SliffDriver.sys"

# lsigetwin_SliffDriver.sys

lsigetwin_SliffDriver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068