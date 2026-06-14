---
id: windows-kernel-tpwsav
namespace: windows:kernel:tpwsav
name: "TPwSav.sys"
description: "A driver associated with Toshiba laptops power saving functionality allows arbitary one byte reading and writing mapped physical addresses. Blackpoint Cyber's SOC observed this driver being used as part of a custom EDRSandblast malware to blind EDR prior to Qilin ransomware deployment."
author: "Robel Campbell"
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
  template: "sc.exe create TPwSav.sys binPath=C:\\windows\\temp\\TPwSav.sys type=kernel && sc.exe start TPwSav.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load TPwSav.sys kernel driver"
    commands:
      - "sc.exe create TPwSav.sys binPath=C:\\windows\\temp\\TPwSav.sys type=kernel && sc.exe start TPwSav.sys"
references:
  - label: "Reference"
    url: "https://blackpointcyber.com/resources/blog/qilin-ransomware-and-the-hidden-dangers-of-byovd/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TPwSav.sys binPath=C:\\\\windows\\\\temp\\\\TPwSav.sys type=kernel && sc.exe start TPwSav.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TPwSav.sys"

# TPwSav.sys

A driver associated with Toshiba laptops power saving functionality allows arbitary one byte reading and writing mapped physical addresses. Blackpoint Cyber's SOC observed this driver being used as part of a custom EDRSandblast malware to blind EDR prior to Qilin ransomware deployment.

**Use Case:** Elevate privileges, Blind EDR

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068