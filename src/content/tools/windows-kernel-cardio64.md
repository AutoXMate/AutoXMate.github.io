---
id: windows-kernel-cardio64
namespace: windows:kernel:cardio64
name: "CardIo64.sys"
description: "CardIo64.sys is a kernel driver from ICP DAS Co., LTD. (Taiwan), an industrial automation and I/O board manufacturer. The driver exposes arbitrary physical memory read/write via MmMapIoSpace, port I/O read/write (8/16/32-bit), and PCI bus data read/write via HalGetBusDataByOffset and HalSetBusDataByOffset. The driver is only 13KB and is also available in the KeServiceDescriptorTable/vulnerable-drivers repository on GitHub."
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
  template: "sc.exe create CardIo binPath=C:\\windows\\temp\\CardIo64.sys type=kernel && sc.exe start CardIo"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load CardIo64.sys kernel driver"
    commands:
      - "sc.exe create CardIo binPath=C:\\windows\\temp\\CardIo64.sys type=kernel && sc.exe start CardIo"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/310"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CardIo binPath=C:\\\\windows\\\\temp\\\\CardIo64.sys type=kernel && sc.exe start CardIo"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CardIo64.sys"

# CardIo64.sys

CardIo64.sys is a kernel driver from ICP DAS Co., LTD. (Taiwan), an industrial automation and I/O board manufacturer. The driver exposes arbitrary physical memory read/write via MmMapIoSpace, port I/O read/write (8/16/32-bit), and PCI bus data read/write via HalGetBusDataByOffset and HalSetBusDataByOffset. The driver is only 13KB and is also available in the KeServiceDescriptorTable/vulnerable-drivers repository on GitHub.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068