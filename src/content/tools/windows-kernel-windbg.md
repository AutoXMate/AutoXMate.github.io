---
id: windows-kernel-windbg
namespace: windows:kernel:windbg
name: windbg.sys
description: Kernel driver seen in a recent CopperStealer campaign.
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
  template: sc.exe create windbg.sys binPath=C:\windows\temp\windbg.sys type=kernel
    && sc.exe start windbg.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load windbg.sys kernel driver
  commands:
  - sc.exe create windbg.sys binPath=C:\windows\temp\windbg.sys type=kernel && sc.exe
    start windbg.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/e1cb86386757b947b39086cc8639da988f6e8018ca9995dd669bdc03c8d39d7d.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/fa9abb3e7e06f857be191a1e049dd37642ec41fb2520c105df2227fcac3de5d5.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/06c5ebd0371342d18bc81a96f5e5ce28de64101e3c2fd0161d0b54d8368d2f1f.yara
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_mal_drivers_strict.yar
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
  url: https://www.proofpoint.com/us/blog/threat-insight/now-you-see-it-now-you-dont-copperstealer-performs-widespread-theft
- label: Reference
  url: https://twitter.com/jaydinbas/status/1642898531445886978?s=20
- label: Reference
  url: https://twitter.com/jaydinbas/status/1646475092006785027?s=20
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create windbg.sys binPath=C:\\\\windows\\\\temp\\\\windbg.sys type=kernel && sc.exe start windbg.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver windbg.sys"

# windbg.sys

Kernel driver seen in a recent CopperStealer campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
