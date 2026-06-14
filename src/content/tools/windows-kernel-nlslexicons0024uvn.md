---
id: windows-kernel-nlslexicons0024uvn
namespace: windows:kernel:nlslexicons0024uvn
name: NlsLexicons0024UvN.sys
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
  template: sc.exe create NlsLexicons0024UvN.sys binPath=C:\windows\temp\NlsLexicons0024UvN.sys
    type=kernel && sc.exe start NlsLexicons0024UvN.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load NlsLexicons0024UvN.sys kernel driver
  commands:
  - sc.exe create NlsLexicons0024UvN.sys binPath=C:\windows\temp\NlsLexicons0024UvN.sys
    type=kernel && sc.exe start NlsLexicons0024UvN.sys
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
    command: "sc.exe create NlsLexicons0024UvN.sys binPath=C:\\\\windows\\\\temp\\\\NlsLexicons0024UvN.sys type=kernel && sc.exe start NlsLexicons0024UvN.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NlsLexicons0024UvN.sys"

# NlsLexicons0024UvN.sys

Cisco Talos has identified multiple versions of an undocumented malicious driver named “RedDriver,” a driver-based browser hijacker that uses the Windows Filtering Platform (WFP) to intercept browser traffic. RedDriver has been active since at least 2021.
RedDriver utilizes HookSignTool to forge its signature timestamp to bypass Windows driver-signing policies.
Code from multiple open-source tools has been used in the development of RedDriver's infection chain, including HP-Socket and a custom implementation of ReflectiveLoader.
The authors of RedDriver appear to be skilled in driver development and have deep knowledge of the Windows operating system.
This threat appears to target native Chinese speakers, as it searches for Chinese language browsers to hijack. Additionally, the authors are likely Chinese speakers themselves.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
