---
id: windows-kernel-pdfwkrnl
namespace: windows:kernel:pdfwkrnl
name: PDFWKRNL.sys
description: AMD USB-C Power Delivery Firmware Update Kernel Library driver with arbitrary
  physical memory read/write capabilities. Identified in ESET EDR killers research
  (March 2026) as actively abused by threat actors to disable EDR products.
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
  template: sc.exe create PDFWKRNL.sys binPath=C:\windows\temp\PDFWKRNL.sys type=kernel
    && sc.exe start PDFWKRNL.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load PDFWKRNL.sys kernel driver
  commands:
  - sc.exe create PDFWKRNL.sys binPath=C:\windows\temp\PDFWKRNL.sys type=kernel &&
    sc.exe start PDFWKRNL.sys
references:
- label: Reference
  url: https://www.welivesecurity.com/en/eset-research/edr-killers-explained/
features:
- file-system
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create PDFWKRNL.sys binPath=C:\\\\windows\\\\temp\\\\PDFWKRNL.sys type=kernel && sc.exe start PDFWKRNL.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver PDFWKRNL.sys"

# PDFWKRNL.sys

AMD USB-C Power Delivery Firmware Update Kernel Library driver with arbitrary physical memory read/write capabilities. Identified in ESET EDR killers research (March 2026) as actively abused by threat actors to disable EDR products.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
