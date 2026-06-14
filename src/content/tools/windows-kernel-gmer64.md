---
id: windows-kernel-gmer64
namespace: windows:kernel:gmer64
name: "gmer64.sys"
description: "Driver used by the GMER application. Which is an application that detects and removes rootkits"
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: "sc.exe create gmer64.sys binPath=C:\\windows\\temp\\gmer64.sys type=kernel && sc.exe start gmer64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load gmer64.sys kernel driver"
    commands:
      - "sc.exe create gmer64.sys binPath=C:\\windows\\temp\\gmer64.sys type=kernel && sc.exe start gmer64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/18c909a2b8c5e16821d6ef908f56881aa0ecceeaccb5fa1e54995935fcfd12f7.yara"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_mal_drivers_strict.yar"
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
    url: "https://github.com/magicsword-io/LOLDrivers/issues/55#issuecomment-1537161951"
  - label: "Reference"
    url: "http://www.gmer.net/"
  - label: "Reference"
    url: "https://github.com/gtworek/PSBits/blob/master/Misc/KillWithLolDriver.ps1"
  - label: "Reference"
    url: "https://github.com/ZeroMemoryEx/Blackout"
  - label: "Reference"
    url: "https://github.com/b1-team/superman"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create gmer64.sys binPath=C:\\\\windows\\\\temp\\\\gmer64.sys type=kernel && sc.exe start gmer64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver gmer64.sys"

# gmer64.sys

Driver used by the GMER application. Which is an application that detects and removes rootkits

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068