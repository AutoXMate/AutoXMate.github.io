---
id: windows-kernel-amsdk
namespace: windows:kernel:amsdk
name: "amsdk.sys"
description: "Vulnerable WatchDog Antimalware driver used by Silver Fox APT group to load unsigned drivers and execute malicious code in kernel mode"
author: "The Haag"
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
  template: "sc.exe create amsdk binPath=C:\\windows\\temp\\amsdk.sys type=kernel && sc.exe start amsdk"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load amsdk.sys kernel driver"
    commands:
      - "sc.exe create amsdk binPath=C:\\windows\\temp\\amsdk.sys type=kernel && sc.exe start amsdk"
references:
  - label: "Reference"
    url: "https://research.checkpoint.com/2025/silver-fox-apt-vulnerable-drivers/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create amsdk binPath=C:\\\\windows\\\\temp\\\\amsdk.sys type=kernel && sc.exe start amsdk"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver amsdk.sys"

# amsdk.sys

Vulnerable WatchDog Antimalware driver used by Silver Fox APT group to load unsigned drivers and execute malicious code in kernel mode

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants