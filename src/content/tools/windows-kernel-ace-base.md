---
id: windows-kernel-ace-base
namespace: windows:kernel:ace-base
name: ACE-BASE.sys
description: Allows privilege escalation from regular user to System or PPL
author: Defence Tech security
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
  template: ''
  sandbox: execFile
  timeout_seconds: 30
  shell: true
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ACE-BASE.sys binPath=C:\\windows\\temp\\ACE-BASE.sys type=kernel && sc.exe start ACE-BASE.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ACE-BASE.sys"

# ACE-BASE.sys

Allows privilege escalation from regular user to System or PPL

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
