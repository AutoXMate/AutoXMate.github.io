---
id: windows-kernel-afd
namespace: windows:kernel:afd
name: Afd.sys
description: Windows Ancillary Function Driver (Afd.sys) for WinSock is vulnerable
  to an Elevation of Privilege Vulnerability.
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
  template: sc.exe create Afd.sys binPath=C:\windows\temp\Afd.sys type=kernel && sc.exe
    start Afd.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Afd.sys kernel driver
  commands:
  - sc.exe create Afd.sys binPath=C:\windows\temp\Afd.sys type=kernel && sc.exe start
    Afd.sys
references:
- label: Reference
  url: https://securityintelligence.com/x-force/patch-tuesday-exploit-wednesday-pwning-windows-ancillary-function-driver-winsock/
- label: Reference
  url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21768
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Afd.sys binPath=C:\\\\windows\\\\temp\\\\Afd.sys type=kernel && sc.exe start Afd.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Afd.sys"

# Afd.sys

Windows Ancillary Function Driver (Afd.sys) for WinSock is vulnerable to an Elevation of Privilege Vulnerability.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
