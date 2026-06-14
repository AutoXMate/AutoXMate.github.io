---
id: windows-kernel-whql
namespace: windows:kernel:whql
name: "whql.sys"
description: "whql.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create whql binPath=C:\\windows\\temp\\whql.sys type=kernel && sc.exe start whql"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load whql.sys kernel driver"
    commands:
      - "sc.exe create whql binPath=C:\\windows\\temp\\whql.sys type=kernel && sc.exe start whql"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create whql binPath=C:\\\\windows\\\\temp\\\\whql.sys type=kernel && sc.exe start whql"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver whql.sys"

# whql.sys

whql.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068