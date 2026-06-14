---
id: windows-kernel-tcio
namespace: windows:kernel:tcio
name: TcIo.sys
description: TcIo.sys and TcRouter.sys are WHQL Microsoft-signed kernel drivers from
  Beckhoff Automation GmbH (TwinCAT 3 Industrial Automation Runtime). TcIo.sys exposes
  arbitrary physical memory read/write via ZwOpenSection on Device\PhysicalMemory,
  arbitrary MMIO mapping via MmMapIoSpace, PCI configuration space read/write via
  HalGetBusDataByOffset and HalSetBusDataByOffset, and full PCI BAR probing and mapping.
  TcRouter.sys exposes arbitrary port I/O via direct ring-0 in/out instructions. Both
  drivers ...
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
  template: sc.exe create TcIo binPath=C:\windows\temp\TcIo.sys type=kernel && sc.exe
    start TcIo
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load TcIo.sys kernel driver
  commands:
  - sc.exe create TcIo binPath=C:\windows\temp\TcIo.sys type=kernel && sc.exe start
    TcIo
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/296
- label: Reference
  url: https://www.cisa.gov/news-events/ics-advisories/icsa-18-081-02
- label: Reference
  url: https://srcincite.io/advisories/src-2018-0007/
- label: Reference
  url: https://nvd.nist.gov/vuln/detail/CVE-2018-7502
features:
- file-system
- network-intensive
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TcIo binPath=C:\\\\windows\\\\temp\\\\TcIo.sys type=kernel && sc.exe start TcIo"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TcIo.sys"

# TcIo.sys

TcIo.sys and TcRouter.sys are WHQL Microsoft-signed kernel drivers from Beckhoff Automation GmbH (TwinCAT 3 Industrial Automation Runtime). TcIo.sys exposes arbitrary physical memory read/write via ZwOpenSection on Device\PhysicalMemory, arbitrary MMIO mapping via MmMapIoSpace, PCI configuration space read/write via HalGetBusDataByOffset and HalSetBusDataByOffset, and full PCI BAR probing and mapping. TcRouter.sys exposes arbitrary port I/O via direct ring-0 in/out instructions. Both drivers use plain IoCreateDevice with no DACL and have no caller validation on IRP_MJ_CREATE. All IOCTLs use METHOD_NEITHER with FILE_ANY_ACCESS. No hardware gate -- drivers load on any x64 Windows without Beckhoff hardware. CVE-2018-7502 was assigned for an untrusted pointer dereference in IOCTL 0x222206 affecting 19 drivers in the TwinCAT family (CISA advisory ICSA-18-081-02, Source Incite SRC-2018-0007). The physical memory and port I/O primitives described here go beyond the scope of CVE-2018-7502. 18 related drivers share the same codebase and certificate.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
