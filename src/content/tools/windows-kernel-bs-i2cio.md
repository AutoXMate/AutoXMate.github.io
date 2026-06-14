---
id: windows-kernel-bs-i2cio
namespace: windows:kernel:bs-i2cio
name: BS_I2cIo.sys
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
  template: sc.exe create BS_I2cIo.sys binPath=C:\windows\temp\BS_I2cIo.sys type=kernel
    && sc.exe start BS_I2cIo.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BS_I2cIo.sys kernel driver
  commands:
  - sc.exe create BS_I2cIo.sys binPath=C:\windows\temp\BS_I2cIo.sys type=kernel &&
    sc.exe start BS_I2cIo.sys
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
    command: "sc.exe create BS_I2cIo.sys binPath=C:\\\\windows\\\\temp\\\\BS_I2cIo.sys type=kernel && sc.exe start BS_I2cIo.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_I2cIo.sys"

# BS_I2cIo.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
