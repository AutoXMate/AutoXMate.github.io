---
id: windows-kernel-npr0
namespace: windows:kernel:npr0
name: "NPR0.sys"
description: "NPR0.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create NPR0 binPath=C:\\windows\\temp\\NPR0.sys type=kernel && sc.exe start NPR0"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load NPR0.sys kernel driver"
    commands:
      - "sc.exe create NPR0 binPath=C:\\windows\\temp\\NPR0.sys type=kernel && sc.exe start NPR0"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NPR0 binPath=C:\\\\windows\\\\temp\\\\NPR0.sys type=kernel && sc.exe start NPR0"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NPR0.sys"

# NPR0.sys

NPR0.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068