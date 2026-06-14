---
id: windows-kernel-proxy32
namespace: windows:kernel:proxy32
name: Proxy32.sys
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
  template: sc.exe create Proxy32.sys binPath=C:\windows\temp\Proxy32.sys type=kernel
    && sc.exe start Proxy32.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Proxy32.sys kernel driver
  commands:
  - sc.exe create Proxy32.sys binPath=C:\windows\temp\Proxy32.sys type=kernel && sc.exe
    start Proxy32.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- remote
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Proxy32.sys binPath=C:\\\\windows\\\\temp\\\\Proxy32.sys type=kernel && sc.exe start Proxy32.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Proxy32.sys"

# Proxy32.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
