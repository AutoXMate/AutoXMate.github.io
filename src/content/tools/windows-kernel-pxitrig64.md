---
id: windows-kernel-pxitrig64
namespace: windows:kernel:pxitrig64
name: pxitrig64.sys
description: Northwave Cyber Security contributed this driver based on in-house research.
  The driver has a CVSSv3 score of 5.5, indicating a local dos impact. This vulnerability
  could potentially be exploited for privilege escalation or other malicious activities.
author: Northwave Cyber Security
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
  template: sc.exe create pxitrig64 binPath=C:\windows\temp\pxitrig64.sys type=kernel
    && sc.exe start pxitrig64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load pxitrig64.sys kernel driver
  commands:
  - sc.exe create pxitrig64 binPath=C:\windows\temp\pxitrig64.sys type=kernel && sc.exe
    start pxitrig64
features:
- local
- pipes-stdin
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create pxitrig64 binPath=C:\\\\windows\\\\temp\\\\pxitrig64.sys type=kernel && sc.exe start pxitrig64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver pxitrig64.sys"

# pxitrig64.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 5.5, indicating a local dos impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
