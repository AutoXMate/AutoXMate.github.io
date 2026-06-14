---
id: windows-kernel-bs-flash64
namespace: windows:kernel:bs-flash64
name: BS_Flash64.sys
description: Elevate privileges
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create BS_Flash64.sys binPath=C:\windows\temp\BS_Flash64.sys type=kernel
    && sc.exe start BS_Flash64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BS_Flash64.sys kernel driver
  commands:
  - sc.exe create BS_Flash64.sys binPath=C:\windows\temp\BS_Flash64.sys type=kernel
    && sc.exe start BS_Flash64.sys
references:
- label: Reference
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_Flash64.sys binPath=C:\\\\windows\\\\temp\\\\BS_Flash64.sys type=kernel && sc.exe start BS_Flash64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_Flash64.sys"

# BS_Flash64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
