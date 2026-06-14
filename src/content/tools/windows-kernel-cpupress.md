---
id: windows-kernel-cpupress
namespace: windows:kernel:cpupress
name: cpupress.sys
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
  template: sc.exe create cpupress.sys binPath=C:\windows\temp\cpupress.sys type=kernel
    && sc.exe start cpupress.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load cpupress.sys kernel driver
  commands:
  - sc.exe create cpupress.sys binPath=C:\windows\temp\cpupress.sys type=kernel &&
    sc.exe start cpupress.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- file-system
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create cpupress.sys binPath=C:\\\\windows\\\\temp\\\\cpupress.sys type=kernel && sc.exe start cpupress.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver cpupress.sys"

# cpupress.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
