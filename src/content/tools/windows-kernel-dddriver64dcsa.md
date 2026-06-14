---
id: windows-kernel-dddriver64dcsa
namespace: windows:kernel:dddriver64dcsa
name: "dddriver64Dcsa.sys"
description: "dddriver64Dcsa.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create dddriver64Dcsa binPath=C:\\windows\\temp\\dddriver64Dcsa.sys type=kernel && sc.exe start dddriver64Dcsa"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load dddriver64Dcsa.sys kernel driver"
    commands:
      - "sc.exe create dddriver64Dcsa binPath=C:\\windows\\temp\\dddriver64Dcsa.sys type=kernel && sc.exe start dddriver64Dcsa"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dddriver64Dcsa binPath=C:\\\\windows\\\\temp\\\\dddriver64Dcsa.sys type=kernel && sc.exe start dddriver64Dcsa"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dddriver64Dcsa.sys"

# dddriver64Dcsa.sys

dddriver64Dcsa.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068