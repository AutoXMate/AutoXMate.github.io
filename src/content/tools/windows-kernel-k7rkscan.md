---
id: windows-kernel-k7rkscan
namespace: windows:kernel:k7rkscan
name: K7RKScan.sys
description: Driver can be used to load unsigned drivers
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
  template: sc.exe create K7RKScan.sys binPath=C:\windows\temp\K7RKScan.sys type=kernel
    && sc.exe start K7RKScan.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load K7RKScan.sys kernel driver
  commands:
  - sc.exe create K7RKScan.sys binPath=C:\windows\temp\K7RKScan.sys type=kernel &&
    sc.exe start K7RKScan.sys
references:
- label: Reference
  url: https://github.com/BlackSnufkin/BYOVD
features:
- network-intensive
- pipes-stdin
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create K7RKScan.sys binPath=C:\\\\windows\\\\temp\\\\K7RKScan.sys type=kernel && sc.exe start K7RKScan.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver K7RKScan.sys"

# K7RKScan.sys

Driver can be used to load unsigned drivers

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
