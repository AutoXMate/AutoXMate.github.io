---
id: windows-kernel-asrautochkupddrv-1-0-32
namespace: windows:kernel:asrautochkupddrv-1-0-32
name: AsrAutoChkUpdDrv_1_0_32.sys
description: Confirmed vulnerable driver from Microsoft Block List
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
  template: ''
  sandbox: execFile
  timeout_seconds: 30
  shell: true
detections:
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
  url: https://gist.github.com/mgraeber-rc/1bde6a2a83237f17b463d051d32e802c
features:
- file-system
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsrAutoChkUpdDrv_1_0_32.sys binPath=C:\\windows\\temp\\AsrAutoChkUpdDrv_1_0_32.sys type=kernel && sc.exe start AsrAutoChkUpdDrv_1_0_32.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsrAutoChkUpdDrv_1_0_32.sys"

# AsrAutoChkUpdDrv_1_0_32.sys

Confirmed vulnerable driver from Microsoft Block List

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
