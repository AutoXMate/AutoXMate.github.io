---
id: windows-kernel-netfilterdrv
namespace: windows:kernel:netfilterdrv
name: netfilterdrv.sys
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
trust_level: verified
execution:
  template: sc.exe create netfilterdrv.sys binPath=C:\windows\temp \n \n \n  etfilterdrv.sys     type=kernel
    type=kernel && sc.exe start netfilterdrv.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load netfilterdrv.sys kernel driver
  commands:
  - sc.exe create netfilterdrv.sys binPath=C:\windows\temp \n \n \n  etfilterdrv.sys     type=kernel
    type=kernel && sc.exe start netfilterdrv.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- pipes-stdin
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create netfilterdrv.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  etfilterdrv.sys     type=kernel type=kernel && sc.exe start netfilterdrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver netfilterdrv.sys"

# netfilterdrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
