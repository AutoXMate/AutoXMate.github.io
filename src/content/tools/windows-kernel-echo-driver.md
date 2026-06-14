---
id: windows-kernel-echo-driver
namespace: windows:kernel:echo-driver
name: "echo_driver.sys"
description: "Bad access controls in Inspect Element Ltd.'s echo_driver.sys allows attacker to gain arbitrary memory read and write, which allows for easy Privilege Escalation via Token Theft."
author: "Protocol & Zach"
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
  template: "sc.exe create echo_driver.sys binPath=C:\\windows\\temp\\echo_driver.sys type=kernel && sc.exe start echo_driver.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load echo_driver.sys kernel driver"
    commands:
      - "sc.exe create echo_driver.sys binPath=C:\\windows\\temp\\echo_driver.sys type=kernel && sc.exe start echo_driver.sys"
references:
  - label: "Reference"
    url: "https://ioctl.fail/echo-ac-writeup/"
  - label: "Reference"
    url: "https://github.com/kite03/echoac-poc/tree/main/PoC"
  - label: "Reference"
    url: "https://github.com/pseuxide/kur"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create echo_driver.sys binPath=C:\\\\windows\\\\temp\\\\echo_driver.sys type=kernel && sc.exe start echo_driver.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver echo_driver.sys"

# echo_driver.sys

Bad access controls in Inspect Element Ltd.'s echo_driver.sys allows attacker to gain arbitrary memory read and write, which allows for easy Privilege Escalation via Token Theft.

**Use Case:** Elevate privileges, arbitrary memory read/write

**Required Privileges:** kernel

**MITRE ATT&CK:** T1134