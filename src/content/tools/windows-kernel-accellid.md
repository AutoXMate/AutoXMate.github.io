---
id: windows-kernel-accellid
namespace: windows:kernel:accellid
name: "AccelLid.sys"
description: "Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 5.5, indicating a localdos impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities."
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
  template: "sc.exe create AccelLid.sys binPath=C:\\windows\\temp\\AccelLid.sys type=kernel && sc.exe start AccelLid.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load AccelLid.sys kernel driver"
    commands:
      - "sc.exe create AccelLid.sys binPath=C:\\windows\\temp\\AccelLid.sys type=kernel && sc.exe start AccelLid.sys"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AccelLid.sys binPath=C:\\\\windows\\\\temp\\\\AccelLid.sys type=kernel && sc.exe start AccelLid.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AccelLid.sys"

# AccelLid.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 5.5, indicating a localdos impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068