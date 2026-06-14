---
id: windows-kernel-chaos-rootkit
namespace: windows:kernel:chaos-rootkit
name: Chaos-Rootkit.sys
description: Chaos-Rootkit is a x64 ring0 rootkit with process hiding, privilege escalation,
  and capabilities for protecting and unprotecting processes, work on the latest Windows
  versions.
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
  template: sc.exe create Chaos-Rootkit.sys binPath=C:\windows\temp\Chaos-Rootkit.sys
    type=kernel && sc.exe start Chaos-Rootkit.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Chaos-Rootkit.sys kernel driver
  commands:
  - sc.exe create Chaos-Rootkit.sys binPath=C:\windows\temp\Chaos-Rootkit.sys type=kernel
    && sc.exe start Chaos-Rootkit.sys
references:
- label: Reference
  url: https://github.com/ZeroMemoryEx/Chaos-Rootkit
features:
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Chaos-Rootkit.sys binPath=C:\\\\windows\\\\temp\\\\Chaos-Rootkit.sys type=kernel && sc.exe start Chaos-Rootkit.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Chaos-Rootkit.sys"

# Chaos-Rootkit.sys

Chaos-Rootkit is a x64 ring0 rootkit with process hiding, privilege escalation, and capabilities for protecting and unprotecting processes, work on the latest Windows versions.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
