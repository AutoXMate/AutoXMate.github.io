---
id: windows-kernel-aida64driver
namespace: windows:kernel:aida64driver
name: "AIDA64Driver.sys"
description: "AIDA64Driver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create AIDA64Driver binPath=C:\\windows\\temp\\AIDA64Driver.sys type=kernel && sc.exe start AIDA64Driver"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load AIDA64Driver.sys kernel driver"
    commands:
      - "sc.exe create AIDA64Driver binPath=C:\\windows\\temp\\AIDA64Driver.sys type=kernel && sc.exe start AIDA64Driver"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AIDA64Driver binPath=C:\\\\windows\\\\temp\\\\AIDA64Driver.sys type=kernel && sc.exe start AIDA64Driver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AIDA64Driver.sys"

# AIDA64Driver.sys

AIDA64Driver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068