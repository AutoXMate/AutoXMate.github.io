---
id: windows-kernel-asribdrv
namespace: windows:kernel:asribdrv
name: AsrIbDrv.sys
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
  template: sc.exe create AsrIbDrv.sys binPath=C:\windows\temp\AsrIbDrv.sys type=kernel
    && sc.exe start AsrIbDrv.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load AsrIbDrv.sys kernel driver
  commands:
  - sc.exe create AsrIbDrv.sys binPath=C:\windows\temp\AsrIbDrv.sys type=kernel &&
    sc.exe start AsrIbDrv.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/2a652de6b680d5ad92376ad323021850dab2c653abf06edf26120f7714b8e08a.yara
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
  url: https://github.com/namazso/physmem_drivers
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsrIbDrv.sys binPath=C:\\\\windows\\\\temp\\\\AsrIbDrv.sys type=kernel && sc.exe start AsrIbDrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsrIbDrv.sys"

# AsrIbDrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
