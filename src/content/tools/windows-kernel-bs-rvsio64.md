---
id: windows-kernel-bs-rvsio64
namespace: windows:kernel:bs-rvsio64
name: "BS_RVSIO64.sys"
description: "BS_RVSIO64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create BS_RVSIO64 binPath=C:\\windows\\temp\\BS_RVSIO64.sys type=kernel && sc.exe start BS_RVSIO64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load BS_RVSIO64.sys kernel driver"
    commands:
      - "sc.exe create BS_RVSIO64 binPath=C:\\windows\\temp\\BS_RVSIO64.sys type=kernel && sc.exe start BS_RVSIO64"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_RVSIO64 binPath=C:\\\\windows\\\\temp\\\\BS_RVSIO64.sys type=kernel && sc.exe start BS_RVSIO64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_RVSIO64.sys"

# BS_RVSIO64.sys

BS_RVSIO64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068