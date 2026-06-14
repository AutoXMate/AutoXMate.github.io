---
id: windows-kernel-driver7-x86-withoutdbg
namespace: windows:kernel:driver7-x86-withoutdbg
name: "driver7-x86-withoutdbg.sys"
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
  template: "sc.exe create driver7-x86-withoutdbg.sys binPath=C:\\windows\\temp\\driver7-x86-withoutdbg.sys     type=kernel && sc.exe start driver7-x86-withoutdbg.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load driver7-x86-withoutdbg.sys kernel driver"
    commands:
      - "sc.exe create driver7-x86-withoutdbg.sys binPath=C:\\windows\\temp\\driver7-x86-withoutdbg.sys     type=kernel && sc.exe start driver7-x86-withoutdbg.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/927c2a580d51a598177fa54c65e9d2610f5f212f1b6cb2fbf2740b64368f010a.yara"
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
    command: "sc.exe create driver7-x86-withoutdbg.sys binPath=C:\\\\windows\\\\temp\\\\driver7-x86-withoutdbg.sys     type=kernel && sc.exe start driver7-x86-withoutdbg.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver driver7-x86-withoutdbg.sys"

# driver7-x86-withoutdbg.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068