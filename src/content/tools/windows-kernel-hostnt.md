---
id: windows-kernel-hostnt
namespace: windows:kernel:hostnt
name: HOSTNT.sys
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
  template: sc.exe create HOSTNT.sys binPath=C:\windows\temp\HOSTNT.sys type=kernel
    && sc.exe start HOSTNT.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load HOSTNT.sys kernel driver
  commands:
  - sc.exe create HOSTNT.sys binPath=C:\windows\temp\HOSTNT.sys type=kernel && sc.exe
    start HOSTNT.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/07b6d69bafcfd767f1b63a490a8843c3bb1f8e1bbea56176109b5743c8f7d357.yara
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
    command: "sc.exe create HOSTNT.sys binPath=C:\\\\windows\\\\temp\\\\HOSTNT.sys type=kernel && sc.exe start HOSTNT.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver HOSTNT.sys"

# HOSTNT.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
