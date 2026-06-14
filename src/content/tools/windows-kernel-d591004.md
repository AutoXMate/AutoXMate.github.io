---
id: windows-kernel-d591004
namespace: windows:kernel:d591004
name: "d591004.sys"
description: "d591004.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create d591004 binPath=C:\\windows\\temp\\d591004.sys type=kernel && sc.exe start d591004"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load d591004.sys kernel driver"
    commands:
      - "sc.exe create d591004 binPath=C:\\windows\\temp\\d591004.sys type=kernel && sc.exe start d591004"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create d591004 binPath=C:\\\\windows\\\\temp\\\\d591004.sys type=kernel && sc.exe start d591004"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver d591004.sys"

# d591004.sys

d591004.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068