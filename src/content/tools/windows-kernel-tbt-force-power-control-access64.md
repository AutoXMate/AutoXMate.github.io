---
id: windows-kernel-tbt-force-power-control-access64
namespace: windows:kernel:tbt-force-power-control-access64
name: TBT_Force_Power_Control_Access64.sys
description: TBT_Force_Power_Control_Access64.sys is a Thunderbolt force power control
  driver from Wistron Corporation that exposes physical memory read/write via MmMapIoSpace.
  Wistron is a major Taiwan-based OEM/ODM. Another Wistron driver (WiRwaDrv.sys) is
  already tracked in LOLDrivers. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers
  repository.
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
  template: sc.exe create TBT_Force_Power_Control_Access64 binPath=C:\windows\temp\TBT_Force_Power_Control_Access64.sys
    type=kernel && sc.exe start TBT_Force_Power_Control_Access64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load TBT_Force_Power_Control_Access64.sys kernel driver
  commands:
  - sc.exe create TBT_Force_Power_Control_Access64 binPath=C:\windows\temp\TBT_Force_Power_Control_Access64.sys
    type=kernel && sc.exe start TBT_Force_Power_Control_Access64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/316
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TBT_Force_Power_Control_Access64 binPath=C:\\\\windows\\\\temp\\\\TBT_Force_Power_Control_Access64.sys type=kernel && sc.exe start TBT_Force_Power_Control_Access64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TBT_Force_Power_Control_Access64.sys"

# TBT_Force_Power_Control_Access64.sys

TBT_Force_Power_Control_Access64.sys is a Thunderbolt force power control driver from Wistron Corporation that exposes physical memory read/write via MmMapIoSpace. Wistron is a major Taiwan-based OEM/ODM. Another Wistron driver (WiRwaDrv.sys) is already tracked in LOLDrivers. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
