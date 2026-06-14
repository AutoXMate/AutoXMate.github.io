---
id: windows-kernel-sysdrv3s
namespace: windows:kernel:sysdrv3s
name: SysDrv3S.sys
description: Vulnerable driver found in https://github.com/hfiref0x/KDU.
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
  template: sc.exe create SysDrv3S.sys binPath=C:\windows\temp\SysDrv3S.sys type=kernel
    && sc.exe start SysDrv3S.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load SysDrv3S.sys kernel driver
  commands:
  - sc.exe create SysDrv3S.sys binPath=C:\windows\temp\SysDrv3S.sys type=kernel &&
    sc.exe start SysDrv3S.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/0e53b58415fa68552928622118d5b8a3a851b2fc512709a90b63ba46acda8b6b.yara
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
  url: https://github.com/magicsword-io/LOLDrivers/issues/55#issuecomment-1537161951
features:
- network-intensive
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SysDrv3S.sys binPath=C:\\\\windows\\\\temp\\\\SysDrv3S.sys type=kernel && sc.exe start SysDrv3S.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SysDrv3S.sys"

# SysDrv3S.sys

Vulnerable driver found in https://github.com/hfiref0x/KDU.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
