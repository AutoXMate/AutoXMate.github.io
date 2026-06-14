---
id: windows-kernel-asromgdrv
namespace: windows:kernel:asromgdrv
name: "AsrOmgDrv.sys"
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
  template: "sc.exe create AsrOmgDrv.sys binPath=C:\\windows\\temp\\AsrOmgDrv.sys type=kernel && sc.exe start AsrOmgDrv.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load AsrOmgDrv.sys kernel driver"
    commands:
      - "sc.exe create AsrOmgDrv.sys binPath=C:\\windows\\temp\\AsrOmgDrv.sys type=kernel && sc.exe start AsrOmgDrv.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/950a4c0c772021cee26011a92194f0e58d61588f77f2873aa0599dff52a160c9.yara"
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
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsrOmgDrv.sys binPath=C:\\\\windows\\\\temp\\\\AsrOmgDrv.sys type=kernel && sc.exe start AsrOmgDrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsrOmgDrv.sys"

# AsrOmgDrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068