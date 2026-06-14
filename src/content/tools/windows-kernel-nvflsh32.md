---
id: windows-kernel-nvflsh32
namespace: windows:kernel:nvflsh32
name: "nvflsh32.sys"
description: "Confirmed vulnerable driver from Microsoft Block List"
author: "Michael Haag"
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
  template: ""
  sandbox: execFile
  timeout_seconds: 30
  shell: true
detections:
  - type: other
references:
  - label: "Reference"
    url: "https://gist.github.com/mgraeber-rc/1bde6a2a83237f17b463d051d32e802c"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nvflsh32.sys binPath=C:\\windows\\temp\\nvflsh32.sys type=kernel && sc.exe start nvflsh32.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nvflsh32.sys"

# nvflsh32.sys

Confirmed vulnerable driver from Microsoft Block List

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068