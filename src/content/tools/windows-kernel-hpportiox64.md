---
id: windows-kernel-hpportiox64
namespace: windows:kernel:hpportiox64
name: HpPortIox64.sys
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
  template: sc.exe create HpPortIox64.sys binPath=C:\windows\temp\HpPortIox64.sys     type=kernel
    && sc.exe start HpPortIox64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load HpPortIox64.sys kernel driver
  commands:
  - sc.exe create HpPortIox64.sys binPath=C:\windows\temp\HpPortIox64.sys     type=kernel
    && sc.exe start HpPortIox64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/c5050a2017490fff7aa53c73755982b339ddb0fd7cef2cde32c81bc9834331c5.yara
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
    command: "sc.exe create HpPortIox64.sys binPath=C:\\\\windows\\\\temp\\\\HpPortIox64.sys     type=kernel && sc.exe start HpPortIox64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver HpPortIox64.sys"

# HpPortIox64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
