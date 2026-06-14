---
id: windows-kernel-testbone
namespace: windows:kernel:testbone
name: TestBone.sys
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
  template: sc.exe create TestBone.sys binPath=C:\windows\temp\TestBone.sys type=kernel
    && sc.exe start TestBone.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load TestBone.sys kernel driver
  commands:
  - sc.exe create TestBone.sys binPath=C:\windows\temp\TestBone.sys type=kernel &&
    sc.exe start TestBone.sys
references:
- label: Reference
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TestBone.sys binPath=C:\\\\windows\\\\temp\\\\TestBone.sys type=kernel && sc.exe start TestBone.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TestBone.sys"

# TestBone.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
