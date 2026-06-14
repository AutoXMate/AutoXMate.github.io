---
id: windows-kernel-goad
namespace: windows:kernel:goad
name: goad.sys
description: Elevate privileges
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: community
execution:
  template: sc.exe create goad.sys binPath=C:\windows\temp\goad.sys type=kernel &&
    sc.exe start goad.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load goad.sys kernel driver
  commands:
  - sc.exe create goad.sys binPath=C:\windows\temp\goad.sys type=kernel && sc.exe
    start goad.sys
references:
- label: Reference
  url: https://github.com/jbaines-r7/dellicious
- label: Reference
  url: https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create goad.sys binPath=C:\\\\windows\\\\temp\\\\goad.sys type=kernel && sc.exe start goad.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver goad.sys"

# goad.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
