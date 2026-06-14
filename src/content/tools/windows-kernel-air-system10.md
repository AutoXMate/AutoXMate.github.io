---
id: windows-kernel-air-system10
namespace: windows:kernel:air-system10
name: Air_SYSTEM10.sys
description: Driver categorized as POORTRY by Mandiant.
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: sc.exe create Air_SYSTEM10.sys binPath=C:\windows\temp\Air_SYSTEM10.sys     type=kernel
    && sc.exe start Air_SYSTEM10.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Air_SYSTEM10.sys kernel driver
  commands:
  - sc.exe create Air_SYSTEM10.sys binPath=C:\windows\temp\Air_SYSTEM10.sys     type=kernel
    && sc.exe start Air_SYSTEM10.sys
references:
- label: Reference
  url: https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware
features:
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Air_SYSTEM10.sys binPath=C:\\\\windows\\\\temp\\\\Air_SYSTEM10.sys     type=kernel && sc.exe start Air_SYSTEM10.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Air_SYSTEM10.sys"

# Air_SYSTEM10.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
