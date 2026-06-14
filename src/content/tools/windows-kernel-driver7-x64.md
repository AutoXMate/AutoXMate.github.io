---
id: windows-kernel-driver7-x64
namespace: windows:kernel:driver7-x64
name: driver7-x64.sys
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
  template: sc.exe create driver7-x64.sys binPath=C:\windows\temp\driver7-x64.sys     type=kernel
    && sc.exe start driver7-x64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load driver7-x64.sys kernel driver
  commands:
  - sc.exe create driver7-x64.sys binPath=C:\windows\temp\driver7-x64.sys     type=kernel
    && sc.exe start driver7-x64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/771a8d05f1af6214e0ef0886662be500ee910ab99f0154227067fddcfe08a3dd.yara
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
  url: https://github.com/Chigusa0w0/AsusDriversPrivEscala
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create driver7-x64.sys binPath=C:\\\\windows\\\\temp\\\\driver7-x64.sys     type=kernel && sc.exe start driver7-x64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver driver7-x64.sys"

# driver7-x64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
