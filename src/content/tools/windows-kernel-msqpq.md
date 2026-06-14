---
id: windows-kernel-msqpq
namespace: windows:kernel:msqpq
name: "MSqPq.sys"
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
trust_level: verified
execution:
  template: "sc.exe create MSqPq.sys binPath=C:\\windows\\temp\\MSqPq.sys type=kernel && sc.exe start MSqPq.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load MSqPq.sys kernel driver"
    commands:
      - "sc.exe create MSqPq.sys binPath=C:\\windows\\temp\\MSqPq.sys type=kernel && sc.exe start MSqPq.sys"
references:
  - label: "Reference"
    url: "https://www.trendmicro.com/en_us/research/23/e/blackcat-ransomware-deploys-new-signed-kernel-driver.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create MSqPq.sys binPath=C:\\\\windows\\\\temp\\\\MSqPq.sys type=kernel && sc.exe start MSqPq.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver MSqPq.sys"

# MSqPq.sys

BlackCat Ransomware Deploys New Signed Kernel Driver. BlackCat ransomware incident that occurred in February 2023.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068