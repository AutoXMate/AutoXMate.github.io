---
id: windows-kernel-cpuz141
namespace: windows:kernel:cpuz141
name: cpuz141.sys
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
  template: sc.exe create cpuz141.sys binPath=C:\windows\temp\cpuz141.sys type=kernel
    && sc.exe start cpuz141.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load cpuz141.sys kernel driver
  commands:
  - sc.exe create cpuz141.sys binPath=C:\windows\temp\cpuz141.sys type=kernel && sc.exe
    start cpuz141.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/ded2927f9a4e64eefd09d0caba78e94f309e3a6292841ae81d5528cab109f95d.yara
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
- file-system
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create cpuz141.sys binPath=C:\\\\windows\\\\temp\\\\cpuz141.sys type=kernel && sc.exe start cpuz141.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver cpuz141.sys"

# cpuz141.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
