---
id: windows-kernel-1fc7aeeff3ab19004d2e53eae8160ab1
namespace: windows:kernel:1fc7aeeff3ab19004d2e53eae8160ab1
name: 1fc7aeeff3ab19004d2e53eae8160ab1.sys
description: Cisco Talos has identified multiple versions of an undocumented malicious
  driver named “RedDriver,” a driver-based browser hijacker that uses the Windows
  Filtering Platform (WFP) to intercept browser traffic. RedDriver has been active
  since at least 2021. RedDriver utilizes HookSignTool to forge its signature timestamp
  to bypass Windows driver-signing policies. Code from multiple open-source tools
  has been used in the development of RedDriver's infection chain, including HP-Socket
  and a custo...
author: Alice Climent-Pommeret
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
  template: sc.exe create 1fc7aeeff3ab19004d2e53eae8160ab1.sys binPath=C:\windows\temp\1fc7aeeff3ab19004d2e53eae8160ab1.sys
    type=kernel && sc.exe start 1fc7aeeff3ab19004d2e53eae8160ab1.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load 1fc7aeeff3ab19004d2e53eae8160ab1.sys kernel driver
  commands:
  - sc.exe create 1fc7aeeff3ab19004d2e53eae8160ab1.sys binPath=C:\windows\temp\1fc7aeeff3ab19004d2e53eae8160ab1.sys
    type=kernel && sc.exe start 1fc7aeeff3ab19004d2e53eae8160ab1.sys
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
    command: "sc.exe create 1fc7aeeff3ab19004d2e53eae8160ab1.sys binPath=C:\\\\windows\\\\temp\\\\1fc7aeeff3ab19004d2e53eae8160ab1.sys type=kernel && sc.exe start 1fc7aeeff3ab19004d2e53eae8160ab1.sys"

# 1fc7aeeff3ab19004d2e53eae8160ab1.sys

Cisco Talos has identified multiple versions of an undocumented malicious driver named “RedDriver,” a driver-based browser hijacker that uses the Windows Filtering Platform (WFP) to intercept browser traffic. RedDriver has been active since at least 2021. RedDriver utilizes HookSignTool to forge its signature timestamp to bypass Windows driver-signing policies. Code from multiple open-source tools has been used in the development of RedDriver's infection chain, including HP-Socket and a custom implementation of ReflectiveLoader. The authors of RedDriver appear to be skilled in driver development and have deep knowledge of the Windows operating system. This threat appears to target native Chinese speakers, as it searches for Chinese language browsers to hijack. Additionally, the authors are likely Chinese speakers themselves.

**Required Privileges:** kernel

**MITRE ATT&CK:** T1014
