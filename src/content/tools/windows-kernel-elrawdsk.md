---
id: windows-kernel-elrawdsk
namespace: windows:kernel:elrawdsk
name: elrawdsk.sys
description: Elevate privileges
author: Michael Haag
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
  template: sc.exe create elrawdsk.sys binPath=C:\windows\temp\elrawdsk.sys type=kernel
    && sc.exe start elrawdsk.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load elrawdsk.sys kernel driver
  commands:
  - sc.exe create elrawdsk.sys binPath=C:\windows\temp\elrawdsk.sys type=kernel &&
    sc.exe start elrawdsk.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/4744df6ac02ff0a3f9ad0bf47b15854bbebb73c936dd02f7c79293a2828406f6.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/5a826b4fa10891cf63aae832fc645ce680a483b915c608ca26cedbb173b1b80a.yara
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
  url: https://github.com/jbaines-r7/dellicious
- label: Reference
  url: https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/
- label: Reference
  url: https://securelist.com/shamoon-the-wiper-further-details-part-ii/57784/
- label: Reference
  url: https://github.com/Yara-Rules/rules/blob/master/malware/MALW_Shamoon.yar
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create elrawdsk.sys binPath=C:\\\\windows\\\\temp\\\\elrawdsk.sys type=kernel && sc.exe start elrawdsk.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver elrawdsk.sys"

# elrawdsk.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
