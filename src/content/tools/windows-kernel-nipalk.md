---
id: windows-kernel-nipalk
namespace: windows:kernel:nipalk
name: nipalk.sys
description: nipalk.sys is the NI-PAL (Platform Abstraction Layer) core kernel driver
  that ships with every National Instruments product including NI-DAQmx, LabVIEW,
  and NI-VISA. The driver uses a single IOCTL gateway (0xABCD03C4) dispatching to
  a two-level service table. The device is created with IoCreateDevice (no DACL) and
  IRP_MJ_CREATE returns STATUS_SUCCESS unconditionally with zero caller validation.
  Exposes arbitrary physical memory read/write to usermode via ZwOpenSection on Device\PhysicalMemory...
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
  template: sc.exe create nipalk binPath=C:\windows\temp\nipalk.sys type=kernel &&
    sc.exe start nipalk
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load nipalk.sys kernel driver
  commands:
  - sc.exe create nipalk binPath=C:\windows\temp\nipalk.sys type=kernel && sc.exe
    start nipalk
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/303
- label: Reference
  url: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/improper-input-validation-in-ni-pal.html
- label: Reference
  url: https://nvd.nist.gov/vuln/detail/CVE-2021-38304
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nipalk binPath=C:\\\\windows\\\\temp\\\\nipalk.sys type=kernel && sc.exe start nipalk"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nipalk.sys"

# nipalk.sys

nipalk.sys is the NI-PAL (Platform Abstraction Layer) core kernel driver that ships with every National Instruments product including NI-DAQmx, LabVIEW, and NI-VISA. The driver uses a single IOCTL gateway (0xABCD03C4) dispatching to a two-level service table. The device is created with IoCreateDevice (no DACL) and IRP_MJ_CREATE returns STATUS_SUCCESS unconditionally with zero caller validation. Exposes arbitrary physical memory read/write to usermode via ZwOpenSection on Device\PhysicalMemory with SECTION_ALL_ACCESS and ZwMapViewOfSection with PAGE_READWRITE, kernel pages mapped to usermode via MmBuildMdlForNonPagedPool and MmMapLockedPagesSpecifyCache, VA-to-PA translation via MmGetPhysicalAddress, contiguous DMA allocation via MmAllocateContiguousMemorySpecifyCache, full bus read/write, and PCI configuration space access. CVE-2021-38304 covers a different vulnerability class (improper input validation in versions prior to 20.0.1f0) but the physical memory mapping primitives documented here go beyond that CVE scope. EV code signing certificate valid until July 2027.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
