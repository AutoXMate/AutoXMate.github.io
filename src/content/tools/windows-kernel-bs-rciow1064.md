---
id: windows-kernel-bs-rciow1064
namespace: windows:kernel:bs-rciow1064
name: BS_RCIOW1064.sys
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
  template: sc.exe create BS_RCIOW1064.sys binPath=C:\windows\temp\BS_RCIOW1064.sys
    type=kernel && sc.exe start BS_RCIOW1064.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BS_RCIOW1064.sys kernel driver
  commands:
  - sc.exe create BS_RCIOW1064.sys binPath=C:\windows\temp\BS_RCIOW1064.sys type=kernel
    && sc.exe start BS_RCIOW1064.sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_RCIOW1064.sys binPath=C:\\\\windows\\\\temp\\\\BS_RCIOW1064.sys type=kernel && sc.exe start BS_RCIOW1064.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_RCIOW1064.sys"

# BS_RCIOW1064.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
