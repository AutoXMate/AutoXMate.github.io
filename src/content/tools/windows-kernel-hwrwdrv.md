---
id: windows-kernel-hwrwdrv
namespace: windows:kernel:hwrwdrv
name: HwRwDrv.sys
description: Hardware read/write driver signed by a revoked Certum certificate (Open
  Source Developer, Jun Liu). Provides arbitrary physical memory read/write and PCI
  bus data access. Identified in ESET EDR killers research (March 2026) with 174 execution
  parents indicating widespread abuse by threat actors to disable EDR products.
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
  template: sc.exe create HwRwDrv.sys binPath=C:\windows\temp\HwRwDrv.sys type=kernel
    && sc.exe start HwRwDrv.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load HwRwDrv.sys kernel driver
  commands:
  - sc.exe create HwRwDrv.sys binPath=C:\windows\temp\HwRwDrv.sys type=kernel && sc.exe
    start HwRwDrv.sys
references:
- label: Reference
  url: https://www.welivesecurity.com/en/eset-research/edr-killers-explained/
features:
- encryption
- file-system
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create HwRwDrv.sys binPath=C:\\\\windows\\\\temp\\\\HwRwDrv.sys type=kernel && sc.exe start HwRwDrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver HwRwDrv.sys"

# HwRwDrv.sys

Hardware read/write driver signed by a revoked Certum certificate (Open Source Developer, Jun Liu). Provides arbitrary physical memory read/write and PCI bus data access. Identified in ESET EDR killers research (March 2026) with 174 execution parents indicating widespread abuse by threat actors to disable EDR products.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
