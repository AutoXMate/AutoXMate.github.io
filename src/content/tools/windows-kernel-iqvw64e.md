---
id: windows-kernel-iqvw64e
namespace: windows:kernel:iqvw64e
name: iqvw64e.sys
description: (1) IQVW32.sys before 1.3.1.0 and (2) IQVW64.sys before 1.3.1.0 in the
  Intel Ethernet diagnostics driver for Windows allows local users to cause a denial
  of service or possibly execute arbitrary code with kernel privileges via a crafted
  (a) 0x80862013, (b) 0x8086200B, (c) 0x8086200F, or (d) 0x80862007 IOCTL call.
author: Michael Haag, Guus Verbeek
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create iqvw64e.sys binPath=C:\windows\temp\iqvw64e.sys type=kernel
    && sc.exe start iqvw64e.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load iqvw64e.sys kernel driver
  commands:
  - sc.exe create iqvw64e.sys binPath=C:\windows\temp\iqvw64e.sys type=kernel && sc.exe
    start iqvw64e.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/4429f32db1cc70567919d7d47b844a91cf1329a6cd116f582305f3b7b60cd60b.yara
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict_renamed.yar
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
references:
- label: Reference
  url: https://www.crowdstrike.com/blog/scattered-spider-attempts-to-avoid-detection-with-bring-your-own-vulnerable-driver-tactic/
- label: Reference
  url: https://expel.com/blog/well-that-escalated-quickly-how-a-red-team-went-from-domain-user-to-kernel-memory/
- label: Reference
  url: https://github.com/Exploitables/CVE-2015-2291
- label: Reference
  url: https://github.com/Tare05/Intel-CVE-2015-2291
- label: Reference
  url: https://github.com/TheCruZ/kdmapper
- label: Reference
  url: https://gist.github.com/k4nfr3/af970e7facb09195e56f2112e1c9549c
features:
- local
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create iqvw64e.sys binPath=C:\\\\windows\\\\temp\\\\iqvw64e.sys type=kernel && sc.exe start iqvw64e.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver iqvw64e.sys"

# iqvw64e.sys

(1) IQVW32.sys before 1.3.1.0 and (2) IQVW64.sys before 1.3.1.0 in the Intel Ethernet diagnostics driver for Windows allows local users to cause a denial of service or possibly execute arbitrary code with kernel privileges via a crafted (a) 0x80862013, (b) 0x8086200B, (c) 0x8086200F, or (d) 0x80862007 IOCTL call.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
