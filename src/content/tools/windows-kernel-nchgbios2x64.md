---
id: windows-kernel-nchgbios2x64
namespace: windows:kernel:nchgbios2x64
name: NCHGBIOS2x64.SYS
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
  template: sc.exe create NCHGBIOS2x64.SYS binPath=C:\windows\temp\NCHGBIOS2x64.SYS     type=kernel
    && sc.exe start NCHGBIOS2x64.SYS
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load NCHGBIOS2x64.SYS kernel driver
  commands:
  - sc.exe create NCHGBIOS2x64.SYS binPath=C:\windows\temp\NCHGBIOS2x64.SYS     type=kernel
    && sc.exe start NCHGBIOS2x64.SYS
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/314384b40626800b1cde6fbc51ebc7d13e91398be2688c2a58354aa08d00b073.yara
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
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NCHGBIOS2x64.SYS binPath=C:\\\\windows\\\\temp\\\\NCHGBIOS2x64.SYS     type=kernel && sc.exe start NCHGBIOS2x64.SYS"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NCHGBIOS2x64.SYS"

# NCHGBIOS2x64.SYS

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
