---
id: windows-kernel-watabe
namespace: windows:kernel:watabe
name: "watabe.sys"
description: "watabe.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create watabe binPath=C:\\windows\\temp\\watabe.sys type=kernel && sc.exe start watabe"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load watabe.sys kernel driver"
    commands:
      - "sc.exe create watabe binPath=C:\\windows\\temp\\watabe.sys type=kernel && sc.exe start watabe"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create watabe binPath=C:\\\\windows\\\\temp\\\\watabe.sys type=kernel && sc.exe start watabe"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver watabe.sys"

# watabe.sys

watabe.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068