---
id: windows-kernel-speedfan
namespace: windows:kernel:speedfan
name: speedfan.sys
description: speedfan.sys is a vulnerable driver. CVE-2007-5633.
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
  template: sc.exe create speedfan.sys binPath=C:\windows\temp\speedfan.sys type=kernel
    && sc.exe start speedfan.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load speedfan.sys kernel driver
  commands:
  - sc.exe create speedfan.sys binPath=C:\windows\temp\speedfan.sys type=kernel &&
    sc.exe start speedfan.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/22be050955347661685a4343c51f11c7811674e030386d2264cd12ecbf544b7c.yara
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
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create speedfan.sys binPath=C:\\\\windows\\\\temp\\\\speedfan.sys type=kernel && sc.exe start speedfan.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver speedfan.sys"

# speedfan.sys

speedfan.sys is a vulnerable driver. CVE-2007-5633.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
