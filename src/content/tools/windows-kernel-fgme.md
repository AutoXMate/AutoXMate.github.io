---
id: windows-kernel-fgme
namespace: windows:kernel:fgme
name: "fgme.sys"
description: "BlackCat Ransomware Deploys New Signed Kernel Driver. BlackCat ransomware incident that occurred in February 2023."
author: "Guus Verbeek"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: community
execution:
  template: "sc.exe create fgme.sys binPath=C:\\windows\\temp\\fgme.sys type=kernel && sc.exe start fgme.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load fgme.sys kernel driver"
    commands:
      - "sc.exe create fgme.sys binPath=C:\\windows\\temp\\fgme.sys type=kernel && sc.exe start fgme.sys"
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_us/research/23/e/blackcat-ransomware-deploys-new-signed-kernel-driver.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create fgme.sys binPath=C:\\\\windows\\\\temp\\\\fgme.sys type=kernel && sc.exe start fgme.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver fgme.sys"

# fgme.sys

BlackCat Ransomware Deploys New Signed Kernel Driver. BlackCat ransomware incident that occurred in February 2023.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068