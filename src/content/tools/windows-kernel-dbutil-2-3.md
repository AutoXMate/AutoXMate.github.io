---
id: windows-kernel-dbutil-2-3
namespace: windows:kernel:dbutil-2-3
name: "dbutil_2_3.sys"
description: "Elevate privileges"
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
  template: "sc.exe create dbutil_2_3.sys binPath=C:\\windows\\temp\\dbutil_2_3.sys type=kernel && sc.exe start dbutil_2_3.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load dbutil_2_3.sys kernel driver"
    commands:
      - "sc.exe create dbutil_2_3.sys binPath=C:\\windows\\temp\\dbutil_2_3.sys type=kernel && sc.exe start dbutil_2_3.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
  - label: "Reference"
    url: "https://www.sentinelone.com/labs/cve-2021-21551-hundreds-of-millions-of-dell-computers-at-risk-due-to-multiple-bios-driver-privilege-escalation-flaws/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dbutil_2_3.sys binPath=C:\\\\windows\\\\temp\\\\dbutil_2_3.sys type=kernel && sc.exe start dbutil_2_3.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dbutil_2_3.sys"

# dbutil_2_3.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068