---
id: windows-kernel-csc
namespace: windows:kernel:csc
name: CSC.sys
description: Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control
  Code in the csc.sys driver
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
  template: sc.exe create CSC.sys binPath=C:\windows\temp\CSC.sys type=kernel && sc.exe
    start CSC.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load CSC.sys kernel driver
  commands:
  - sc.exe create CSC.sys binPath=C:\windows\temp\CSC.sys type=kernel && sc.exe start
    CSC.sys
references:
- label: Reference
  url: https://github.com/varwara/CVE-2024-26229/tree/main
- label: Reference
  url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-26229
- label: Reference
  url: https://github.com/zer0condition/ZeroHVCI
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CSC.sys binPath=C:\\\\windows\\\\temp\\\\CSC.sys type=kernel && sc.exe start CSC.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CSC.sys"

# CSC.sys

Improper Address Validation in IOCTL with METHOD_NEITHER I/O Control Code in the csc.sys driver

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
