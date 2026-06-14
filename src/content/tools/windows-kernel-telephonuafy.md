---
id: windows-kernel-telephonuafy
namespace: windows:kernel:telephonuafy
name: telephonuAfY.sys
description: Cisco Talos has identified multiple versions of an undocumented malicious
  driver named “RedDriver,” a driver-based browser hijacker that uses the Windows
  Filtering Platform (WFP) to intercept browser traffic. RedDriver has been active
  since at least 2021. RedDriver utilizes HookSignTool to forge its signature timestamp
  to bypass Windows driver-signing policies. Code from multiple open-source tools
  has been used in the development of RedDriver's infection chain, including HP-Socket
  and a custo...
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: sc.exe create telephonuAfY.sys binPath=C:\windows\temp\telephonuAfY.sys
    type=kernel && sc.exe start telephonuAfY.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load telephonuAfY.sys kernel driver
  commands:
  - sc.exe create telephonuAfY.sys binPath=C:\windows\temp\telephonuAfY.sys type=kernel
    && sc.exe start telephonuAfY.sys
references:
- label: Reference
  url: https://blog.talosintelligence.com/undocumented-reddriver/
features:
- file-system
- pipes-stdin
- requires-root
- stealth
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create telephonuAfY.sys binPath=C:\\\\windows\\\\temp\\\\telephonuAfY.sys type=kernel && sc.exe start telephonuAfY.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver telephonuAfY.sys"

# telephonuAfY.sys

Cisco Talos has identified multiple versions of an undocumented malicious driver named “RedDriver,” a driver-based browser hijacker that uses the Windows Filtering Platform (WFP) to intercept browser traffic. RedDriver has been active since at least 2021.
RedDriver utilizes HookSignTool to forge its signature timestamp to bypass Windows driver-signing policies.
Code from multiple open-source tools has been used in the development of RedDriver's infection chain, including HP-Socket and a custom implementation of ReflectiveLoader.
The authors of RedDriver appear to be skilled in driver development and have deep knowledge of the Windows operating system.
This threat appears to target native Chinese speakers, as it searches for Chinese language browsers to hijack. Additionally, the authors are likely Chinese speakers themselves.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
