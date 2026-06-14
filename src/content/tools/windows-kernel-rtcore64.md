---
id: windows-kernel-rtcore64
namespace: windows:kernel:rtcore64
name: RTCore64.sys
description: Elevate privileges
author: Nasreddine Bencherchali
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
  template: sc.exe create RTCore64.sys binPath=C:\windows\temp\RTCore64.sys type=kernel
    && sc.exe start RTCore64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load RTCore64.sys kernel driver
  commands:
  - sc.exe create RTCore64.sys binPath=C:\windows\temp\RTCore64.sys type=kernel &&
    sc.exe start RTCore64.sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create RTCore64.sys binPath=C:\\\\windows\\\\temp\\\\RTCore64.sys type=kernel && sc.exe start RTCore64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver RTCore64.sys"

# RTCore64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
