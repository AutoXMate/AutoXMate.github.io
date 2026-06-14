---
id: windows-kernel-asrcddrv
namespace: windows:kernel:asrcddrv
name: AsrCDDrv.sys
description: AsrCDDrv.sys is a kernel driver from ASRock Incorporation that exposes
  control register read/write (cr0, cr2, cr3, cr4, cr8), arbitrary MSR read/write,
  arbitrary physical memory read/write via MmMapIoSpace, contiguous memory allocation/free
  via MmAllocateContiguousMemorySpecifyCache, and I/O port read/write (8/16/32-bit).
  The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.
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
  template: sc.exe create AsrCDDrv binPath=C:\windows\temp\AsrCDDrv.sys type=kernel
    && sc.exe start AsrCDDrv
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load AsrCDDrv.sys kernel driver
  commands:
  - sc.exe create AsrCDDrv binPath=C:\windows\temp\AsrCDDrv.sys type=kernel && sc.exe
    start AsrCDDrv
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/326
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsrCDDrv binPath=C:\\\\windows\\\\temp\\\\AsrCDDrv.sys type=kernel && sc.exe start AsrCDDrv"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsrCDDrv.sys"

# AsrCDDrv.sys

AsrCDDrv.sys is a kernel driver from ASRock Incorporation that exposes control register read/write (cr0, cr2, cr3, cr4, cr8), arbitrary MSR read/write, arbitrary physical memory read/write via MmMapIoSpace, contiguous memory allocation/free via MmAllocateContiguousMemorySpecifyCache, and I/O port read/write (8/16/32-bit). The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
