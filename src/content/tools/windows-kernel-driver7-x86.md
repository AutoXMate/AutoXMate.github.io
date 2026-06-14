---
id: windows-kernel-driver7-x86
namespace: windows:kernel:driver7-x86
name: "driver7-x86.sys"
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
  template: "sc.exe create driver7-x86.sys binPath=C:\\windows\\temp\\driver7-x86.sys     type=kernel && sc.exe start driver7-x86.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load driver7-x86.sys kernel driver"
    commands:
      - "sc.exe create driver7-x86.sys binPath=C:\\windows\\temp\\driver7-x86.sys     type=kernel && sc.exe start driver7-x86.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/42851a01469ba97cdc38939b10cf9ea13237aa1f6c37b1ac84904c5a12a81fa0.yara"
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
    url: "https://github.com/Chigusa0w0/AsusDriversPrivEscala"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create driver7-x86.sys binPath=C:\\\\windows\\\\temp\\\\driver7-x86.sys     type=kernel && sc.exe start driver7-x86.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver driver7-x86.sys"

# driver7-x86.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068