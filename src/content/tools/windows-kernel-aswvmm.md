---
id: windows-kernel-aswvmm
namespace: windows:kernel:aswvmm
name: aswVmm.sys
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
  template: sc.exe create aswVmm.sys binPath=C:\windows\temp\aswVmm.sys type=kernel
    && sc.exe start aswVmm.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load aswVmm.sys kernel driver
  commands:
  - sc.exe create aswVmm.sys binPath=C:\windows\temp\aswVmm.sys type=kernel && sc.exe
    start aswVmm.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/36505921af5a09175395ebaea29c72b2a69a3a9204384a767a5be8a721f31b10.yara
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
  url: https://github.com/tanduRE/AvastHV
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create aswVmm.sys binPath=C:\\\\windows\\\\temp\\\\aswVmm.sys type=kernel && sc.exe start aswVmm.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver aswVmm.sys"

# aswVmm.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
