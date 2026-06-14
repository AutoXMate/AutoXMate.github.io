---
id: windows-kernel-rtkio
namespace: windows:kernel:rtkio
name: rtkio.sys
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
  template: sc.exe create rtkio64.sys binPath=C:\windows\temp\rtkio64.sys type=kernel
    && sc.exe start rtkio64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load rtkio.sys kernel driver
  commands:
  - sc.exe create rtkio64.sys binPath=C:\windows\temp\rtkio64.sys type=kernel && sc.exe
    start rtkio64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/074ae477c8c7ae76c6f2b0bf77ac17935a8e8ee51b52155d2821d93ab30f3761.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/916c535957a3b8cbf3336b63b2260ea4055163a9e6b214f2a7005d6d36a4a677.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/ab8f2217e59319b88080e052782e559a706fa4fb7b8b708f709ff3617124da89.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/caa85c44eb511377ea7426ff10df00a701c07ffb384eef8287636a4bca0b53ab.yara
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
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=rtkio
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create rtkio64.sys binPath=C:\\\\windows\\\\temp\\\\rtkio64.sys type=kernel && sc.exe start rtkio64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver rtkio.sys"

# rtkio.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
