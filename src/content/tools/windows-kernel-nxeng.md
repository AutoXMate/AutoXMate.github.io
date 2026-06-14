---
id: windows-kernel-nxeng
namespace: windows:kernel:nxeng
name: "nxeng.sys"
description: "nxeng.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create nxeng binPath=C:\\windows\\temp\\nxeng.sys type=kernel && sc.exe start nxeng"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nxeng.sys kernel driver"
    commands:
      - "sc.exe create nxeng binPath=C:\\windows\\temp\\nxeng.sys type=kernel && sc.exe start nxeng"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nxeng binPath=C:\\\\windows\\\\temp\\\\nxeng.sys type=kernel && sc.exe start nxeng"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nxeng.sys"

# nxeng.sys

nxeng.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068