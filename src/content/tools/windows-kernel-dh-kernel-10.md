---
id: windows-kernel-dh-kernel-10
namespace: windows:kernel:dh-kernel-10
name: Dh_Kernel_10.sys
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
  template: sc.exe create Dh_Kernel_10.sys binPath=C:\windows\temp\Dh_Kernel_10.sys     type=kernel
    && sc.exe start Dh_Kernel_10.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Dh_Kernel_10.sys kernel driver
  commands:
  - sc.exe create Dh_Kernel_10.sys binPath=C:\windows\temp\Dh_Kernel_10.sys     type=kernel
    && sc.exe start Dh_Kernel_10.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/80cbba9f404df3e642f22c476664d63d7c229d45d34f5cd0e19c65eb41becec3.yara
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
  url: https://github.com/namazso/physmem_drivers
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Dh_Kernel_10.sys binPath=C:\\\\windows\\\\temp\\\\Dh_Kernel_10.sys     type=kernel && sc.exe start Dh_Kernel_10.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Dh_Kernel_10.sys"

# Dh_Kernel_10.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
