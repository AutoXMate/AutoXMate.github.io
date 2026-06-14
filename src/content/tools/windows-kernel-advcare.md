---
id: windows-kernel-advcare
namespace: windows:kernel:advcare
name: AdvCare.sys
description: AdvCare.sys is a legacy hardware health monitor driver from Advantech
  Co., Ltd. for industrial PCs and embedded boards. The driver exposes arbitrary MSR
  read/write (wrmsr/rdmsr with no validation), arbitrary physical memory read/write
  via MmMapIoSpace, unrestricted port I/O across all 65536 ports, and PCI configuration
  space read/write via HalGetBusDataByOffset/HalSetBusDataByOffset. The device is
  created with IoCreateDevice (no DACL) and IRP_MJ_CREATE returns STATUS_SUCCESS unconditionally
  w...
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
  template: sc.exe create AdvCare binPath=C:\windows\temp\AdvCare.sys type=kernel
    && sc.exe start AdvCare
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load AdvCare.sys kernel driver
  commands:
  - sc.exe create AdvCare binPath=C:\windows\temp\AdvCare.sys type=kernel && sc.exe
    start AdvCare
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/306
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- requires-root
- streaming
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AdvCare binPath=C:\\\\windows\\\\temp\\\\AdvCare.sys type=kernel && sc.exe start AdvCare"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AdvCare.sys"

# AdvCare.sys

AdvCare.sys is a legacy hardware health monitor driver from Advantech Co., Ltd. for industrial PCs and embedded boards. The driver exposes arbitrary MSR read/write (wrmsr/rdmsr with no validation), arbitrary physical memory read/write via MmMapIoSpace, unrestricted port I/O across all 65536 ports, and PCI configuration space read/write via HalGetBusDataByOffset/HalSetBusDataByOffset. The device is created with IoCreateDevice (no DACL) and IRP_MJ_CREATE returns STATUS_SUCCESS unconditionally with zero caller validation -- no admin check, no token check, no integrity check. Any unprivileged local user can open the device and invoke every primitive. The driver is also available in the KeServiceDescriptorTable/vulnerable-drivers repository on GitHub.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
