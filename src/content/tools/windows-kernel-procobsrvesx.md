---
id: windows-kernel-procobsrvesx
namespace: windows:kernel:procobsrvesx
name: "ProcObsrvesx.sys"
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
  template: "sc.exe create ProcObsrvesx binPath=C:\\windows\\temp\\ProcObsrvesx.sys type=kernel && sc.exe start ProcObsrvesx"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ProcObsrvesx.sys kernel driver"
    commands:
      - "sc.exe create ProcObsrvesx binPath=C:\\windows\\temp\\ProcObsrvesx.sys type=kernel && sc.exe start ProcObsrvesx"
references:
  - label: "Reference"
    url: "https://northwave-cybersecurity.com/vulnerability-notice-escan-antivirus"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ProcObsrvesx binPath=C:\\\\windows\\\\temp\\\\ProcObsrvesx.sys type=kernel && sc.exe start ProcObsrvesx"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ProcObsrvesx.sys"

# ProcObsrvesx.sys

Northwave Cyber Security contributed this driver based on in-house research. The driver has a CVSSv3 score of 8.8, indicating a privilege escalation impact. This vulnerability could potentially be exploited for privilege escalation or other malicious activities.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068