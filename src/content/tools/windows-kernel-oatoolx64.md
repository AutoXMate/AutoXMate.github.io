---
id: windows-kernel-oatoolx64
namespace: windows:kernel:oatoolx64
name: "OAToolx64.sys"
description: "OAToolx64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create OAToolx64 binPath=C:\\windows\\temp\\OAToolx64.sys type=kernel && sc.exe start OAToolx64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load OAToolx64.sys kernel driver"
    commands:
      - "sc.exe create OAToolx64 binPath=C:\\windows\\temp\\OAToolx64.sys type=kernel && sc.exe start OAToolx64"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create OAToolx64 binPath=C:\\\\windows\\\\temp\\\\OAToolx64.sys type=kernel && sc.exe start OAToolx64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver OAToolx64.sys"

# OAToolx64.sys

OAToolx64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068