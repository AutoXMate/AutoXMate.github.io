---
id: windows-kernel-se64a
namespace: windows:kernel:se64a
name: "Se64a.sys"
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
  template: "sc.exe create Se64a.sys binPath=C:\\windows\\temp\\Se64a.sys type=kernel && sc.exe start Se64a.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load Se64a.sys kernel driver"
    commands:
      - "sc.exe create Se64a.sys binPath=C:\\windows\\temp\\Se64a.sys type=kernel && sc.exe start Se64a.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/6cb51ae871fbd5d07c5aad6ff8eea43d34063089528603ca9ceb8b4f52f68ddc.yara"
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
    command: "sc.exe create Se64a.sys binPath=C:\\\\windows\\\\temp\\\\Se64a.sys type=kernel && sc.exe start Se64a.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Se64a.sys"

# Se64a.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068