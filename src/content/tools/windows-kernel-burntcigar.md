---
id: windows-kernel-burntcigar
namespace: windows:kernel:burntcigar
name: "burntcigar.sys"
description: "BurntCigar (aka POORTRY) is a malicious kernel-mode rootkit driver used by multiple ransomware groups including Cuba, BlackCat, Medusa, LockBit, and RansomHub. Designed to disable and remove EDR solutions by terminating security processes and deleting critical security software files. VMProtect-packed driver signed with stolen Blueone Technology certificate. Detected by 32.9% of AV engines. Facilitates ransomware deployment by rendering systems defenseless."
author: "Michael Haag"
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
  template: "sc.exe create burntcigar binPath=C:\\windows\\temp\\burntcigar.sys type=kernel && sc.exe start burntcigar"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load burntcigar.sys kernel driver"
    commands:
      - "sc.exe create burntcigar binPath=C:\\windows\\temp\\burntcigar.sys type=kernel && sc.exe start burntcigar"
references:
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/7c5329b842cc3eaf1ec6c11b00e09a8c5e38ad14134b40a8bae3eda0a167a919"
  - label: "Reference"
    url: "https://news.sophos.com/en-us/2024/08/27/burnt-cigar-2/"
  - label: "Reference"
    url: "https://www.fortiguard.com/threat-signal-report/4920"
  - label: "Reference"
    url: "https://securelist.com/cuba-ransomware/110533/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create burntcigar binPath=C:\\\\windows\\\\temp\\\\burntcigar.sys type=kernel && sc.exe start burntcigar"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver burntcigar.sys"

# burntcigar.sys

BurntCigar (aka POORTRY) is a malicious kernel-mode rootkit driver used by multiple ransomware groups including Cuba, BlackCat, Medusa, LockBit, and RansomHub. Designed to disable and remove EDR solutions by terminating security processes and deleting critical security software files. VMProtect-packed driver signed with stolen Blueone Technology certificate. Detected by 32.9% of AV engines. Facilitates ransomware deployment by rendering systems defenseless.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068