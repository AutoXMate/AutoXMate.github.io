---
id: windows-kernel-bdapiutil
namespace: windows:kernel:bdapiutil
name: BdApiUtil.sys
description: Driver can be used to load unsigned drivers. IOCTL code which takes a
  PID and terminates it (arbitrary process termination). Admin privileges required
  to install the driver, but if it's already installed, can be called by any user
  (non admin).
author: christopher-ellis-workday, plisskien, Julian Pena
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
  template: sc.exe create BdApiUtil.sys binPath=C:\windows\temp\BdApiUtil.sys type=kernel
    && sc.exe start BdApiUtil.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BdApiUtil.sys kernel driver
  commands:
  - sc.exe create BdApiUtil.sys binPath=C:\windows\temp\BdApiUtil.sys type=kernel
    && sc.exe start BdApiUtil.sys
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/204
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/231
- label: Reference
  url: https://github.com/RainbowDynamix/GoodBaiii
- label: Reference
  url: https://blog.talosintelligence.com/byovd-loader-deadlock-ransomware/
features:
- file-system
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BdApiUtil.sys binPath=C:\\\\windows\\\\temp\\\\BdApiUtil.sys type=kernel && sc.exe start BdApiUtil.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BdApiUtil.sys"

# BdApiUtil.sys

Driver can be used to load unsigned drivers. IOCTL code which takes a PID and terminates it (arbitrary process termination). Admin privileges required to install the driver, but if it's already installed, can be called by any user (non admin).

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
