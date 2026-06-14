---
id: windows-kernel-seasunprotect
namespace: windows:kernel:seasunprotect
name: "SeasunProtect.sys"
description: "Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privilege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities."
author: "Northwave Cyber Security"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: "sc.exe create SeasunProtect binPath=C:\\windows\\temp\\SeasunProtect.sys type=kernel && sc.exe start SeasunProtect"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load SeasunProtect.sys kernel driver"
    commands:
      - "sc.exe create SeasunProtect binPath=C:\\windows\\temp\\SeasunProtect.sys type=kernel && sc.exe start SeasunProtect"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SeasunProtect binPath=C:\\\\windows\\\\temp\\\\SeasunProtect.sys type=kernel && sc.exe start SeasunProtect"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SeasunProtect.sys"

# SeasunProtect.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privilege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068