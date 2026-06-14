---
id: windows-kernel-ipctype
namespace: windows:kernel:ipctype
name: "ipctype.sys"
description: "ipctype.sys is a kernel driver from Digital Electronics Corporation that exposes physical memory read/write via MmMapIoSpace. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository."
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
  template: "sc.exe create ipctype binPath=C:\\windows\\temp\\ipctype.sys type=kernel && sc.exe start ipctype"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ipctype.sys kernel driver"
    commands:
      - "sc.exe create ipctype binPath=C:\\windows\\temp\\ipctype.sys type=kernel && sc.exe start ipctype"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/313"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ipctype binPath=C:\\\\windows\\\\temp\\\\ipctype.sys type=kernel && sc.exe start ipctype"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ipctype.sys"

# ipctype.sys

ipctype.sys is a kernel driver from Digital Electronics Corporation that exposes physical memory read/write via MmMapIoSpace. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068