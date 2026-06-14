---
id: windows-kernel-mtcbsv64
namespace: windows:kernel:mtcbsv64
name: "mtcBSv64.sys"
description: "Elevate privileges"
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: "sc.exe create mtcBSv64.sys binPath=C:\\windows\\temp\\mtcBSv64.sys type=kernel && sc.exe start mtcBSv64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load mtcBSv64.sys kernel driver"
    commands:
      - "sc.exe create mtcBSv64.sys binPath=C:\\windows\\temp\\mtcBSv64.sys type=kernel && sc.exe start mtcBSv64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/c9cf1d627078f63a36bbde364cd0d5f2be1714124d186c06db5bcdf549a109f8.yara"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict_renamed.yar"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
references:
  - label: "Reference"
    url: "https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mtcBSv64.sys binPath=C:\\\\windows\\\\temp\\\\mtcBSv64.sys type=kernel && sc.exe start mtcBSv64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver mtcBSv64.sys"

# mtcBSv64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068