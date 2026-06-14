---
id: windows-kernel-wsftprm
namespace: windows:kernel:wsftprm
name: "wsftprm.sys"
description: "Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 6.1, indicating a antivirus killer impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities."
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
  template: "sc.exe create wsftprm binPath=C:\\windows\\temp\\wsftprm.sys type=kernel && sc.exe start wsftprm"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load wsftprm.sys kernel driver"
    commands:
      - "sc.exe create wsftprm binPath=C:\\windows\\temp\\wsftprm.sys type=kernel && sc.exe start wsftprm"
references:
  - label: "Reference"
    url: "https://northwave-cybersecurity.com/vulnerability-notice-topaz-antifraud"
  - label: "Reference"
    url: "https://github.com/xM0kht4r/AV-EDR-Killer"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create wsftprm binPath=C:\\\\windows\\\\temp\\\\wsftprm.sys type=kernel && sc.exe start wsftprm"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wsftprm.sys"

# wsftprm.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 6.1, indicating a antivirus killer impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068