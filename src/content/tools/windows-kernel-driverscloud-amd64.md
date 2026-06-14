---
id: windows-kernel-driverscloud-amd64
namespace: windows:kernel:driverscloud-amd64
name: DriversCloud_amd64.sys
description: CYBELSOFT DriversCloud_amd64.sys exposes 7 IOCTLs with no access checks
  and a zero security descriptor on the device object, meaning any user (including
  low-integrity processes) can open a handle. Primitives include arbitrary physical
  memory read via MmMapIoSpace (up to 2MB per call), arbitrary MSR read/write (including
  IA32_LSTAR for instant kernel code execution), arbitrary I/O port read/write, and
  arbitrary PCI configuration space read/write. A full LSTAR hijack PoC with crash-safe
  ROP res...
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
  template: sc.exe create DriversCloud_amd64 binPath=C:\windows\temp\DriversCloud_amd64.sys
    type=kernel && sc.exe start DriversCloud_amd64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load DriversCloud_amd64.sys kernel driver
  commands:
  - sc.exe create DriversCloud_amd64 binPath=C:\windows\temp\DriversCloud_amd64.sys
    type=kernel && sc.exe start DriversCloud_amd64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/284
- label: Reference
  url: https://www.virustotal.com/gui/file/2bc72d11fa0beda25dc1dbc372967db49bd3c3a3903913f0877bff6792724dfe
features:
- compression
- file-system
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create DriversCloud_amd64 binPath=C:\\\\windows\\\\temp\\\\DriversCloud_amd64.sys type=kernel && sc.exe start DriversCloud_amd64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver DriversCloud_amd64.sys"

# DriversCloud_amd64.sys

CYBELSOFT DriversCloud_amd64.sys exposes 7 IOCTLs with no access checks and a zero security descriptor on the device object, meaning any user (including low-integrity processes) can open a handle. Primitives include arbitrary physical memory read via MmMapIoSpace (up to 2MB per call), arbitrary MSR read/write (including IA32_LSTAR for instant kernel code execution), arbitrary I/O port read/write, and arbitrary PCI configuration space read/write. A full LSTAR hijack PoC with crash-safe ROP restore has been demonstrated. The developer acknowledged the issue and is working on a rewritten driver.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
