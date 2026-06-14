---
id: windows-kernel-gftkyj64
namespace: windows:kernel:gftkyj64
name: gftkyj64.sys
description: SentinelOne has observed prominent threat actors abusing legitimately
  signed Microsoft drivers in active intrusions into telecommunication, BPO, MSSP,
  and financial services businesses. Investigations into these intrusions led to the
  discovery of POORTRY and STONESTOP malware, part of a small toolkit designed to
  terminate AV and EDR processes. We first reported our discovery to Microsoft’s Security
  Response Center (MSRC) in October 2022 and received an official case number (75361).
  Today, MSR...
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
  template: sc.exe create gftkyj64.sys binPath=C:\windows\temp\gftkyj64.sys type=kernel
    && sc.exe start gftkyj64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load gftkyj64.sys kernel driver
  commands:
  - sc.exe create gftkyj64.sys binPath=C:\windows\temp\gftkyj64.sys type=kernel &&
    sc.exe start gftkyj64.sys
references:
- label: Reference
  url: https://www.sentinelone.com/labs/driving-through-defenses-targeted-attacks-leverage-signed-malicious-microsoft-drivers/
features:
- file-system
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create gftkyj64.sys binPath=C:\\\\windows\\\\temp\\\\gftkyj64.sys type=kernel && sc.exe start gftkyj64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver gftkyj64.sys"

# gftkyj64.sys

SentinelOne has observed prominent threat actors abusing legitimately signed Microsoft drivers in active intrusions into telecommunication, BPO, MSSP, and financial services businesses.
Investigations into these intrusions led to the discovery of POORTRY and STONESTOP malware, part of a small toolkit designed to terminate AV and EDR processes.
We first reported our discovery to Microsoft’s Security Response Center (MSRC) in October 2022 and received an official case number (75361). Today, MSRC released an associated advisory under ADV220005.
This research is being released alongside Mandiant, a SentinelOne technology and incident response partner. 

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
