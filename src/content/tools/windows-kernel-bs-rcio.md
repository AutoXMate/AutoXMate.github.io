---
id: windows-kernel-bs-rcio
namespace: windows:kernel:bs-rcio
name: BS_RCIO.sys
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
  template: sc.exe create BS_RCIO.sys binPath=C:\windows\temp\BS_RCIO.sys type=kernel
    && sc.exe start BS_RCIO.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BS_RCIO.sys kernel driver
  commands:
  - sc.exe create BS_RCIO.sys binPath=C:\windows\temp\BS_RCIO.sys type=kernel && sc.exe
    start BS_RCIO.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_RCIO.sys binPath=C:\\\\windows\\\\temp\\\\BS_RCIO.sys type=kernel && sc.exe start BS_RCIO.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_RCIO.sys"

# BS_RCIO.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
