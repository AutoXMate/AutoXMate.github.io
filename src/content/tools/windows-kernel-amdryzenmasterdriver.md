---
id: windows-kernel-amdryzenmasterdriver
namespace: windows:kernel:amdryzenmasterdriver
name: AMDRyzenMasterDriver.sys
description: Elevate privileges
author: Michael Haag, Nasreddine Bencherchali
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
  template: sc.exe create AMDRyzenMasterDriver.sys binPath=C:\windows\temp\AMDRyzenMasterDriver.sys
    type=kernel && sc.exe start AMDRyzenMasterDriver.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load AMDRyzenMasterDriver.sys kernel driver
  commands:
  - sc.exe create AMDRyzenMasterDriver.sys binPath=C:\windows\temp\AMDRyzenMasterDriver.sys
    type=kernel && sc.exe start AMDRyzenMasterDriver.sys
detections:
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
  url: https://github.com/elastic/protections-artifacts/search?q=AMDRyzenMasterDriver
- label: Reference
  url: https://github.com/NtGabrielGomes/CVE-2023-20564
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AMDRyzenMasterDriver.sys binPath=C:\\\\windows\\\\temp\\\\AMDRyzenMasterDriver.sys type=kernel && sc.exe start AMDRyzenMasterDriver.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AMDRyzenMasterDriver.sys"

# AMDRyzenMasterDriver.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
