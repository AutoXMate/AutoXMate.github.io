---
id: windows-kernel-changsha
namespace: windows:kernel:changsha
name: changsha
description: Malicious rootkit masquerading as legitimate CrowdStrike Falcon Sensor
  driver (CSAgent.sys). Signed with stolen/expired Chinese certificate from 2015.
  Detected by 61.6% of AV engines as Rootkit.Win64.Agent and Trojan:Win64/AVTamper.
  Used to establish kernel-level persistence while evading detection by impersonating
  trusted security software.
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
  template: sc.exe create changsha binPath=C:\windows\temp\changsha.sys type=kernel
    && sc.exe start changsha
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load changsha kernel driver
  commands:
  - sc.exe create changsha binPath=C:\windows\temp\changsha.sys type=kernel && sc.exe
    start changsha
references:
- label: Reference
  url: https://www.virustotal.com/gui/file/06eccd102c9105957773b32538943531d9c39d0a504ceb3b9b155e97e3b0b134
features:
- encryption
- pipes-stdin
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create changsha binPath=C:\\\\windows\\\\temp\\\\changsha.sys type=kernel && sc.exe start changsha"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver changsha"

# changsha

Malicious rootkit masquerading as legitimate CrowdStrike Falcon Sensor driver (CSAgent.sys). Signed with stolen/expired Chinese certificate from 2015. Detected by 61.6% of AV engines as Rootkit.Win64.Agent and Trojan:Win64/AVTamper. Used to establish kernel-level persistence while evading detection by impersonating trusted security software.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
