---
id: windows-kernel-vsdatant
namespace: windows:kernel:vsdatant
name: "vsdatant.sys"
description: "Check Point ZoneAlarm driver (vsdatant.sys) abused in BYOVD attacks to gain kernel privileges and bypass protections such as Memory Integrity."
author: "Kyaw Pyiyt Htet"
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
  template: "sc.exe create vsdatant binPath=C:\\Windows\\Temp\\vsdatant.sys type=kernel && sc.exe start vsdatant"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load vsdatant.sys kernel driver"
    commands:
      - "sc.exe create vsdatant binPath=C:\\Windows\\Temp\\vsdatant.sys type=kernel && sc.exe start vsdatant"
references:
  - label: "Reference"
    url: "https://venaksecurity.com/2025/03/20/cybercriminals-exploit-checkpoints-driver-in-a-byovd-attack/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create vsdatant binPath=C:\\\\Windows\\\\Temp\\\\vsdatant.sys type=kernel && sc.exe start vsdatant"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver vsdatant.sys"

# vsdatant.sys

Check Point ZoneAlarm driver (vsdatant.sys) abused in BYOVD attacks to gain kernel privileges and bypass protections such as Memory Integrity.

**Use Case:** BYOVD (kernel) privilege escalation / defense evasion

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068