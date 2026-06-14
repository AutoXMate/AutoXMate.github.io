---
id: windows-kernel-viverraudio
namespace: windows:kernel:viverraudio
name: ViveRRAudio.sys
description: Northwave Cyber Security contributed this driver based on in-house research.
  The driver has a CVSSv3 score of 5.5, indicating a information disclosure / local
  dos impact. This vulnerability could potentially be exploited for privilege escalation
  or other malicious activities.
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
  template: sc.exe create ViveRRAudio binPath=C:\windows\temp\ViveRRAudio.sys type=kernel
    && sc.exe start ViveRRAudio
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ViveRRAudio.sys kernel driver
  commands:
  - sc.exe create ViveRRAudio binPath=C:\windows\temp\ViveRRAudio.sys type=kernel
    && sc.exe start ViveRRAudio
references:
- label: Reference
  url: https://northwave-cybersecurity.com/vive-vr-headset-kernel-driver-vulnerable-for-out-of-bounds-memory-read
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ViveRRAudio binPath=C:\\\\windows\\\\temp\\\\ViveRRAudio.sys type=kernel && sc.exe start ViveRRAudio"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ViveRRAudio.sys"

# ViveRRAudio.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 5.5, indicating a information disclosure / local dos impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
