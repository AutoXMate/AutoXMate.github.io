---
id: windows-kernel-rtstpx
namespace: windows:kernel:rtstpx
name: "RtsTpx.sys"
description: "RtsTpx.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create RtsTpx binPath=C:\\windows\\temp\\RtsTpx.sys type=kernel && sc.exe start RtsTpx"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load RtsTpx.sys kernel driver"
    commands:
      - "sc.exe create RtsTpx binPath=C:\\windows\\temp\\RtsTpx.sys type=kernel && sc.exe start RtsTpx"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create RtsTpx binPath=C:\\\\windows\\\\temp\\\\RtsTpx.sys type=kernel && sc.exe start RtsTpx"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver RtsTpx.sys"

# RtsTpx.sys

RtsTpx.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068