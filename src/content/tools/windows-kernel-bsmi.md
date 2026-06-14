---
id: windows-kernel-bsmi
namespace: windows:kernel:bsmi
name: BSMI.sys
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
  template: sc.exe create BSMI.sys binPath=C:\windows\temp\BSMI.sys type=kernel &&
    sc.exe start BSMI.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BSMI.sys kernel driver
  commands:
  - sc.exe create BSMI.sys binPath=C:\windows\temp\BSMI.sys type=kernel && sc.exe
    start BSMI.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/59626cac380d8fe0b80a6d4c4406d62ba0683a2f0f68d50ad506ca1b1cf25347.yara
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
- label: Reference
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BSMI.sys binPath=C:\\\\windows\\\\temp\\\\BSMI.sys type=kernel && sc.exe start BSMI.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BSMI.sys"

# BSMI.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
