---
id: windows-kernel-cpqsysio64
namespace: windows:kernel:cpqsysio64
name: cpqsysio64.sys
description: cpqsysio64.sys is a Hewlett-Packard physical memory driver that ships
  as part of the HP ProLiant Support Pack and HP firmware ROM update utilities. The
  driver exposes physical memory read via MmMapIoSpace (IOCTL 0x152EF0) and physical
  memory allocation and mapping to usermode via ZwOpenSection on Device\PhysicalMemory
  combined with ZwMapViewOfSection (IOCTL 0x153E80). The Compaq heritage driver name
  (cpq prefix) dates to the HP-Compaq acquisition. The driver is only 15KB and is
  also available...
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
  template: sc.exe create cpqsysio binPath=C:\windows\temp\cpqsysio64.sys type=kernel
    && sc.exe start cpqsysio
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load cpqsysio64.sys kernel driver
  commands:
  - sc.exe create cpqsysio binPath=C:\windows\temp\cpqsysio64.sys type=kernel && sc.exe
    start cpqsysio
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/311
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- network-intensive
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create cpqsysio binPath=C:\\\\windows\\\\temp\\\\cpqsysio64.sys type=kernel && sc.exe start cpqsysio"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver cpqsysio64.sys"

# cpqsysio64.sys

cpqsysio64.sys is a Hewlett-Packard physical memory driver that ships as part of the HP ProLiant Support Pack and HP firmware ROM update utilities. The driver exposes physical memory read via MmMapIoSpace (IOCTL 0x152EF0) and physical memory allocation and mapping to usermode via ZwOpenSection on Device\PhysicalMemory combined with ZwMapViewOfSection (IOCTL 0x153E80). The Compaq heritage driver name (cpq prefix) dates to the HP-Compaq acquisition. The driver is only 15KB and is also available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
