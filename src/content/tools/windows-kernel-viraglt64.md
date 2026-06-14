---
id: windows-kernel-viraglt64
namespace: windows:kernel:viraglt64
name: "viraglt64.sys"
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
  template: "sc.exe create viraglt64.sys binPath=C:\\windows\\temp\\viraglt64.sys type=kernel && sc.exe start viraglt64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load viraglt64.sys kernel driver"
    commands:
      - "sc.exe create viraglt64.sys binPath=C:\\windows\\temp\\viraglt64.sys type=kernel && sc.exe start viraglt64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/58a74dceb2022cd8a358b92acd1b48a5e01c524c3b0195d7033e4bd55eff4495.yara"
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
    url: "https://github.com/jbaines-r7/dellicious"
  - label: "Reference"
    url: "https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create viraglt64.sys binPath=C:\\\\windows\\\\temp\\\\viraglt64.sys type=kernel && sc.exe start viraglt64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver viraglt64.sys"

# viraglt64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068