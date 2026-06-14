---
id: windows-kernel-kt2
namespace: windows:kernel:kt2
name: "kt2.sys"
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
  template: "sc.exe create kt2.sys binPath=C:\\windows\\temp\\kt2.sys type=kernel && sc.exe start kt2.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load kt2.sys kernel driver"
    commands:
      - "sc.exe create kt2.sys binPath=C:\\windows\\temp\\kt2.sys type=kernel && sc.exe start kt2.sys"
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_us/research/23/e/blackcat-ransomware-deploys-new-signed-kernel-driver.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create kt2.sys binPath=C:\\\\windows\\\\temp\\\\kt2.sys type=kernel && sc.exe start kt2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver kt2.sys"

# kt2.sys

BlackCat Ransomware Deploys New Signed Kernel Driver. BlackCat ransomware incident that occurred in February 2023.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068