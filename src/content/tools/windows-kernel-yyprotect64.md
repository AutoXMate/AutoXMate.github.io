---
id: windows-kernel-yyprotect64
namespace: windows:kernel:yyprotect64
name: "yyprotect64.sys"
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
    command: "sc.exe create yyprotect64.sys binPath=C:\\windows\\temp\\yyprotect64.sys type=kernel && sc.exe start yyprotect64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver yyprotect64.sys"

# yyprotect64.sys

Confirmed vulnerable driver from Microsoft Block List

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068