---
id: windows-kernel-bin-intigua-driver64
namespace: windows:kernel:bin-intigua-driver64
name: "bin_intigua_driver64.sys"
description: "bin_intigua_driver64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create bin_intigua_driver64 binPath=C:\\windows\\temp\\bin_intigua_driver64.sys type=kernel && sc.exe start bin_intigua_driver64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load bin_intigua_driver64.sys kernel driver"
    commands:
      - "sc.exe create bin_intigua_driver64 binPath=C:\\windows\\temp\\bin_intigua_driver64.sys type=kernel && sc.exe start bin_intigua_driver64"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create bin_intigua_driver64 binPath=C:\\\\windows\\\\temp\\\\bin_intigua_driver64.sys type=kernel && sc.exe start bin_intigua_driver64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver bin_intigua_driver64.sys"

# bin_intigua_driver64.sys

bin_intigua_driver64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068