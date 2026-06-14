---
id: windows-kernel-dcprotect
namespace: windows:kernel:dcprotect
name: "DcProtect.sys"
description: "bundled with chinese application \"DrvCeo\" is a set of rootkits. The malicious functionality. prevents registry value writing where the registry key or value includes \"dcprotect\" or \"drvceo\". Prevents file deletion if pathname contains \"driverdownload\", \"program files\\sysceo\", \"program files (x86)\\sysceo\""
author: "Wack0"
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
  template: "sc.exe create DcProtect.sys binPath=C:\\windows\\temp\\DcProtect.sys type=kernel && sc.exe start DcProtect.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load DcProtect.sys kernel driver"
    commands:
      - "sc.exe create DcProtect.sys binPath=C:\\windows\\temp\\DcProtect.sys type=kernel && sc.exe start DcProtect.sys"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/154"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/user/slipstream"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create DcProtect.sys binPath=C:\\\\windows\\\\temp\\\\DcProtect.sys type=kernel && sc.exe start DcProtect.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver DcProtect.sys"

# DcProtect.sys

bundled with chinese application "DrvCeo" is a set of rootkits. The malicious functionality. prevents registry value writing where the registry key or value includes "dcprotect" or "drvceo". Prevents file deletion if pathname contains "driverdownload", "program files\sysceo", "program files (x86)\sysceo"

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068