---
id: windows-kernel-windows-memory-informer
namespace: windows:kernel:windows-memory-informer
name: "Windows-Memory-Informer.sys"
description: "Windows-Memory-Informer.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create Windows-Memory-Informer binPath=C:\\windows\\temp\\Windows-Memory-Informer.sys type=kernel && sc.exe start Windows-Memory-Informer"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load Windows-Memory-Informer.sys kernel driver"
    commands:
      - "sc.exe create Windows-Memory-Informer binPath=C:\\windows\\temp\\Windows-Memory-Informer.sys type=kernel && sc.exe start Windows-Memory-Informer"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Windows-Memory-Informer binPath=C:\\\\windows\\\\temp\\\\Windows-Memory-Informer.sys type=kernel && sc.exe start Windows-Memory-Informer"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Windows-Memory-Informer.sys"

# Windows-Memory-Informer.sys

Windows-Memory-Informer.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068