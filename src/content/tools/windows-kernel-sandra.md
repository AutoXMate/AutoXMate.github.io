---
id: windows-kernel-sandra
namespace: windows:kernel:sandra
name: SANDRA.sys
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
  template: sc.exe create SANDRA binPath=C:\windows\temp\SANDRA type=kernel && sc.exe
    start SANDRA
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load SANDRA.sys kernel driver
  commands:
  - sc.exe create SANDRA binPath=C:\windows\temp\SANDRA type=kernel && sc.exe start
    SANDRA
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
    command: "sc.exe create SANDRA binPath=C:\\\\windows\\\\temp\\\\SANDRA type=kernel && sc.exe start SANDRA"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SANDRA.sys"

# SANDRA.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
