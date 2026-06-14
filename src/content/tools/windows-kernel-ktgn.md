---
id: windows-kernel-ktgn
namespace: windows:kernel:ktgn
name: ktgn.sys
description: BlackCat Ransomware Deploys New Signed Kernel Driver. BlackCat ransomware
  incident that occurred in February 2023.
author: Guus Verbeek
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: critical
trust_level: community
execution:
  template: sc.exe create ktgn.sys binPath=C:\windows\temp\ktgn.sys type=kernel &&
    sc.exe start ktgn.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ktgn.sys kernel driver
  commands:
  - sc.exe create ktgn.sys binPath=C:\windows\temp\ktgn.sys type=kernel && sc.exe
    start ktgn.sys
references:
- label: Reference
  url: https://www.trendmicro.com/en_us/research/23/e/blackcat-ransomware-deploys-new-signed-kernel-driver.html
features:
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ktgn.sys binPath=C:\\\\windows\\\\temp\\\\ktgn.sys type=kernel && sc.exe start ktgn.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ktgn.sys"

# ktgn.sys

BlackCat Ransomware Deploys New Signed Kernel Driver. BlackCat ransomware incident that occurred in February 2023.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
