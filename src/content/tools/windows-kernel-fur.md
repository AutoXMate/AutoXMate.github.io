---
id: windows-kernel-fur
namespace: windows:kernel:fur
name: "fur.sys"
description: "SophosLabs has discovered that threat actors are using a new driver loader called BURNTCIGAR to install a malicious driver signed with Microsoft."
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
  template: "sc.exe create fur.sys binPath=C:\\windows\\temp\\fur.sys type=kernel && sc.exe start fur.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load fur.sys kernel driver"
    commands:
      - "sc.exe create fur.sys binPath=C:\\windows\\temp\\fur.sys type=kernel && sc.exe start fur.sys"
references:
  - label: "Reference"
    url: "https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware, https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create fur.sys binPath=C:\\\\windows\\\\temp\\\\fur.sys type=kernel && sc.exe start fur.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver fur.sys"

# fur.sys

SophosLabs has discovered that threat actors are using a new driver loader called BURNTCIGAR to install a malicious driver signed with Microsoft.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068