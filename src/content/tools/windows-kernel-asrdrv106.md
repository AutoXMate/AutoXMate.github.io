---
id: windows-kernel-asrdrv106
namespace: windows:kernel:asrdrv106
name: AsrDrv106.sys
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
  template: sc.exe create AsrDrv106.sys binPath=C:\windows\temp\AsrDrv106.sys type=kernel
    && sc.exe start AsrDrv106.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load AsrDrv106.sys kernel driver
  commands:
  - sc.exe create AsrDrv106.sys binPath=C:\windows\temp\AsrDrv106.sys type=kernel
    && sc.exe start AsrDrv106.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/3943a796cc7c5352aa57ccf544295bfd6fb69aae147bc8235a00202dc6ed6838.yara
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
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsrDrv106.sys binPath=C:\\\\windows\\\\temp\\\\AsrDrv106.sys type=kernel && sc.exe start AsrDrv106.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsrDrv106.sys"

# AsrDrv106.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
