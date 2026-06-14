---
id: windows-kernel-glckio2
namespace: windows:kernel:glckio2
name: GLCKIO2.sys
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
  template: sc.exe create GLCKIO2.sys binPath=C:\windows\temp\GLCKIO2.sys type=kernel
    && sc.exe start GLCKIO2.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load GLCKIO2.sys kernel driver
  commands:
  - sc.exe create GLCKIO2.sys binPath=C:\windows\temp\GLCKIO2.sys type=kernel && sc.exe
    start GLCKIO2.sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create GLCKIO2.sys binPath=C:\\\\windows\\\\temp\\\\GLCKIO2.sys type=kernel && sc.exe start GLCKIO2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver GLCKIO2.sys"

# GLCKIO2.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
