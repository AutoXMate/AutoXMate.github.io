---
id: windows-kernel-sparkio
namespace: windows:kernel:sparkio
name: SparkIO.sys
description: SparkIO.sys is a WHQL-signed kernel driver from Clevo Co. (Taiwan ODM)
  that ships with Control Center 3.0 and Flexicharger utilities on Clevo-chassis laptops
  (XMG, Eluktronics, EVOO, Origin PC, System76, Sager, and others). CVE-2022-37415
  (CVSS 7.8) documents an out-of-bounds write vulnerability. The driver exposes arbitrary
  physical memory read via MmMapIoSpace, unrestricted I/O port read/write, arbitrary
  PCI configuration space read/write, and SMBus/I2C read/write. The device is created
  wit...
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
  template: sc.exe create SparkIO binPath=C:\windows\temp\SparkIO.sys type=kernel
    && sc.exe start SparkIO
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load SparkIO.sys kernel driver
  commands:
  - sc.exe create SparkIO binPath=C:\windows\temp\SparkIO.sys type=kernel && sc.exe
    start SparkIO
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/322
- label: Reference
  url: https://nvd.nist.gov/vuln/detail/CVE-2022-37415
- label: Reference
  url: https://gist.github.com/alfarom256/220cb75816ca2b5556e7fc8d8d2803a0
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SparkIO binPath=C:\\\\windows\\\\temp\\\\SparkIO.sys type=kernel && sc.exe start SparkIO"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SparkIO.sys"

# SparkIO.sys

SparkIO.sys is a WHQL-signed kernel driver from Clevo Co. (Taiwan ODM) that ships with Control Center 3.0 and Flexicharger utilities on Clevo-chassis laptops (XMG, Eluktronics, EVOO, Origin PC, System76, Sager, and others). CVE-2022-37415 (CVSS 7.8) documents an out-of-bounds write vulnerability. The driver exposes arbitrary physical memory read via MmMapIoSpace, unrestricted I/O port read/write, arbitrary PCI configuration space read/write, and SMBus/I2C read/write. The device is created with IoCreateDevice (no DACL) and IRP_MJ_CREATE returns STATUS_SUCCESS unconditionally with zero caller validation. A public PoC exists by alfarom256.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
