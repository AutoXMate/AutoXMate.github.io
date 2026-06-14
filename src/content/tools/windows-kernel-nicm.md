---
id: windows-kernel-nicm
namespace: windows:kernel:nicm
name: NICM.SYS
description: Elevate privileges
author: Nasreddine Bencherchali
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
  template: sc.exe create NICM.sys binPath=C:\windows\temp\NICM.SYS type=kernel &&
    sc.exe start NICM.SYS
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load NICM.SYS kernel driver
  commands:
  - sc.exe create NICM.sys binPath=C:\windows\temp\NICM.SYS type=kernel && sc.exe
    start NICM.SYS
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
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NICM.sys binPath=C:\\\\windows\\\\temp\\\\NICM.SYS type=kernel && sc.exe start NICM.SYS"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NICM.SYS"

# NICM.SYS

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
