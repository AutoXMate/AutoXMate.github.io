---
id: windows-kernel-proxy64
namespace: windows:kernel:proxy64
name: Proxy64.sys
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
  template: sc.exe create Proxy64.sys binPath=C:\windows\temp\Proxy64.sys type=kernel
    && sc.exe start Proxy64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Proxy64.sys kernel driver
  commands:
  - sc.exe create Proxy64.sys binPath=C:\windows\temp\Proxy64.sys type=kernel && sc.exe
    start Proxy64.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- remote
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Proxy64.sys binPath=C:\\\\windows\\\\temp\\\\Proxy64.sys type=kernel && sc.exe start Proxy64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Proxy64.sys"

# Proxy64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
