---
id: windows-kernel-psmounterex
namespace: windows:kernel:psmounterex
name: "psmounterex.sys"
description: "Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privelege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities."
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
  template: "sc.exe create psmounterex binPath=C:\\windows\\temp\\psmounterex.sys type=kernel && sc.exe start psmounterex"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load psmounterex.sys kernel driver"
    commands:
      - "sc.exe create psmounterex binPath=C:\\windows\\temp\\psmounterex.sys type=kernel && sc.exe start psmounterex"
references:
  - label: "Reference"
    url: "https://northwave-cybersecurity.com/exploiting-enterprise-backup-software-for-privilege-escalation-part-one"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create psmounterex binPath=C:\\\\windows\\\\temp\\\\psmounterex.sys type=kernel && sc.exe start psmounterex"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver psmounterex.sys"

# psmounterex.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privelege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068