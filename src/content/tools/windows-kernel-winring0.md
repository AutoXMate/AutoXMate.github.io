---
id: windows-kernel-winring0
namespace: windows:kernel:winring0
name: WinRing0.sys
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
  template: sc.exe create WinRing0.sys binPath=C:\windows\temp\WinRing0.sys type=kernel
    && sc.exe start WinRing0.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinRing0.sys kernel driver
  commands:
  - sc.exe create WinRing0.sys binPath=C:\windows\temp\WinRing0.sys type=kernel &&
    sc.exe start WinRing0.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/3ec5ad51e6879464dfbccb9f4ed76c6325056a42548d5994ba869da9c4c039a8.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/47eaebc920ccf99e09fc9924feb6b19b8a28589f52783327067c9b09754b5e84.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/a7b000abbcc344444a9b00cfade7aa22ab92ce0cadec196c30eb1851ae4fa062.yara
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
- label: Reference
  url: https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinRing0.sys binPath=C:\\\\windows\\\\temp\\\\WinRing0.sys type=kernel && sc.exe start WinRing0.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinRing0.sys"

# WinRing0.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
