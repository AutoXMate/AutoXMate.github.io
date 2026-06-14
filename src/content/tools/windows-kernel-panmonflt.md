---
id: windows-kernel-panmonflt
namespace: windows:kernel:panmonflt
name: PanMonFlt.sys
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
trust_level: community
execution:
  template: sc.exe create PanMonFlt.sys binPath=C:\windows\temp\PanMonFlt.sys type=kernel
    && sc.exe start PanMonFlt.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load PanMonFlt.sys kernel driver
  commands:
  - sc.exe create PanMonFlt.sys binPath=C:\windows\temp\PanMonFlt.sys type=kernel
    && sc.exe start PanMonFlt.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/7e0124fcc7c95fdc34408cf154cb41e654dade8b898c71ad587b2090b1da30d7.yara
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
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create PanMonFlt.sys binPath=C:\\\\windows\\\\temp\\\\PanMonFlt.sys type=kernel && sc.exe start PanMonFlt.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver PanMonFlt.sys"

# PanMonFlt.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
