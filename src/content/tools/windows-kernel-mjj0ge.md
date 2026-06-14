---
id: windows-kernel-mjj0ge
namespace: windows:kernel:mjj0ge
name: mJj0ge.sys
description: The criminals signed their AV-killer malware, closely related to one
  known as BURNTCIGAR, with a legitimate WHCP certificate
author: Guus Verbeek
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
  template: sc.exe create mJj0ge.sys binPath=C:\windows\temp\mJj0ge.sys type=kernel
    && sc.exe start mJj0ge.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load mJj0ge.sys kernel driver
  commands:
  - sc.exe create mJj0ge.sys binPath=C:\windows\temp\mJj0ge.sys type=kernel && sc.exe
    start mJj0ge.sys
references:
- label: Reference
  url: https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/
features:
- encryption
- file-system
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mJj0ge.sys binPath=C:\\\\windows\\\\temp\\\\mJj0ge.sys type=kernel && sc.exe start mJj0ge.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver mJj0ge.sys"

# mJj0ge.sys

The criminals signed their AV-killer malware, closely related to one known as BURNTCIGAR, with a legitimate WHCP certificate

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
