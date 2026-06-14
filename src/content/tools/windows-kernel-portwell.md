---
id: windows-kernel-portwell
namespace: windows:kernel:portwell
name: portwell.sys
description: portwell.sys is a kernel driver from Portwell Inc. (Taiwan) that exposes
  physical memory read/write via MmMapIoSpace. Portwell manufactures embedded computing
  platforms and industrial PCs. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers
  repository.
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create portwell binPath=C:\windows\temp\portwell.sys type=kernel
    && sc.exe start portwell
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load portwell.sys kernel driver
  commands:
  - sc.exe create portwell binPath=C:\windows\temp\portwell.sys type=kernel && sc.exe
    start portwell
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/314
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create portwell binPath=C:\\\\windows\\\\temp\\\\portwell.sys type=kernel && sc.exe start portwell"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver portwell.sys"

# portwell.sys

portwell.sys is a kernel driver from Portwell Inc. (Taiwan) that exposes physical memory read/write via MmMapIoSpace. Portwell manufactures embedded computing platforms and industrial PCs. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
