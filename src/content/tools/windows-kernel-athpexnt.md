---
id: windows-kernel-athpexnt
namespace: windows:kernel:athpexnt
name: athpexnt.sys
description: AhnLab kernel driver exposing arbitrary physical memory read/write via
  IOCTL 0x81000000. Device accessible at \\.\ATHpEx. Signed by AhnLab Inc. with VeriSign
  certificate (first seen 2014). Zero detections (0/73) on VirusTotal but exploitable
  for privilege escalation by mapping attacker-controlled physical memory into kernel
  address space.
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
  template: sc.exe create ATHpExNt binPath=C:\windows\temp\ATHpExNt.sys type=kernel
    && sc.exe start ATHpExNt
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load athpexnt.sys kernel driver
  commands:
  - sc.exe create ATHpExNt binPath=C:\windows\temp\ATHpExNt.sys type=kernel && sc.exe
    start ATHpExNt
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/255
features:
- encryption
- file-system
- network-intensive
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ATHpExNt binPath=C:\\\\windows\\\\temp\\\\ATHpExNt.sys type=kernel && sc.exe start ATHpExNt"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver athpexnt.sys"

# athpexnt.sys

AhnLab kernel driver exposing arbitrary physical memory read/write via IOCTL 0x81000000. Device accessible at \\.\ATHpEx. Signed by AhnLab Inc. with VeriSign certificate (first seen 2014). Zero detections (0/73) on VirusTotal but exploitable for privilege escalation by mapping attacker-controlled physical memory into kernel address space.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
