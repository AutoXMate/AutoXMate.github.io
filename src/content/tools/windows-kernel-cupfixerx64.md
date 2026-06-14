---
id: windows-kernel-cupfixerx64
namespace: windows:kernel:cupfixerx64
name: CupFixerx64.sys
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
  template: sc.exe create CupFixerx64.sys binPath=C:\windows\temp\CupFixerx64.sys
    type=kernel && sc.exe start CupFixerx64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load CupFixerx64.sys kernel driver
  commands:
  - sc.exe create CupFixerx64.sys binPath=C:\windows\temp\CupFixerx64.sys type=kernel
    && sc.exe start CupFixerx64.sys
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
    command: "sc.exe create CupFixerx64.sys binPath=C:\\\\windows\\\\temp\\\\CupFixerx64.sys type=kernel && sc.exe start CupFixerx64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CupFixerx64.sys"

# CupFixerx64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
