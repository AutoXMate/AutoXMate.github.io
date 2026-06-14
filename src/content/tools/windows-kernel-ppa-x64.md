---
id: windows-kernel-ppa-x64
namespace: windows:kernel:ppa-x64
name: ppa_x64.sys
description: ppa_x64.sys is a kernel driver by Remko Weijnen that provides physical
  memory access via the PhysicalMemory section object. The device name PhyMem indicates
  this is part of the PhyMem driver family, of which several variants are already
  tracked in LOLDrivers (phymem64.sys, Phymemx64.sys, phymem_ext64.sys). The driver
  is available in the KeServiceDescriptorTable/vulnerable-drivers repository.
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
  template: sc.exe create ppa_x64 binPath=C:\windows\temp\ppa_x64.sys type=kernel
    && sc.exe start ppa_x64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ppa_x64.sys kernel driver
  commands:
  - sc.exe create ppa_x64 binPath=C:\windows\temp\ppa_x64.sys type=kernel && sc.exe
    start ppa_x64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/315
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
    command: "sc.exe create ppa_x64 binPath=C:\\\\windows\\\\temp\\\\ppa_x64.sys type=kernel && sc.exe start ppa_x64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ppa_x64.sys"

# ppa_x64.sys

ppa_x64.sys is a kernel driver by Remko Weijnen that provides physical memory access via the PhysicalMemory section object. The device name PhyMem indicates this is part of the PhyMem driver family, of which several variants are already tracked in LOLDrivers (phymem64.sys, Phymemx64.sys, phymem_ext64.sys). The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
