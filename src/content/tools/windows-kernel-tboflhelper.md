---
id: windows-kernel-tboflhelper
namespace: windows:kernel:tboflhelper
name: "tboflhelper.sys"
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
  template: "sc.exe create tboflhelper binPath=C:\\windows\\temp\\tboflhelper.sys type=kernel && sc.exe start tboflhelper"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load tboflhelper.sys kernel driver"
    commands:
      - "sc.exe create tboflhelper binPath=C:\\windows\\temp\\tboflhelper.sys type=kernel && sc.exe start tboflhelper"
references:
  - label: "Reference"
    url: "https://northwave-cybersecurity.com/vulnerability-notice-terabyte-image-for-windows?hsLang=en"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create tboflhelper binPath=C:\\\\windows\\\\temp\\\\tboflhelper.sys type=kernel && sc.exe start tboflhelper"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver tboflhelper.sys"

# tboflhelper.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privelege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068