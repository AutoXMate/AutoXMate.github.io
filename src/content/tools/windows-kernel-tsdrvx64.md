---
id: windows-kernel-tsdrvx64
namespace: windows:kernel:tsdrvx64
name: "TSDRVX64.sys"
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
  template: "sc.exe create TSDRVX64 binPath=C:\\windows\\temp\\TSDRVX64.sys type=kernel && sc.exe start TSDRVX64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load TSDRVX64.sys kernel driver"
    commands:
      - "sc.exe create TSDRVX64 binPath=C:\\windows\\temp\\TSDRVX64.sys type=kernel && sc.exe start TSDRVX64"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TSDRVX64 binPath=C:\\\\windows\\\\temp\\\\TSDRVX64.sys type=kernel && sc.exe start TSDRVX64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TSDRVX64.sys"

# TSDRVX64.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privilege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068