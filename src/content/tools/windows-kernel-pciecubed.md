---
id: windows-kernel-pciecubed
namespace: windows:kernel:pciecubed
name: PcieCubed.sys
description: Driver categorized as POORTRY by Mandiant.
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: sc.exe create PcieCubed.sys binPath=C:\windows\temp\PcieCubed.sys type=kernel
    && sc.exe start PcieCubed.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load PcieCubed.sys kernel driver
  commands:
  - sc.exe create PcieCubed.sys binPath=C:\windows\temp\PcieCubed.sys type=kernel
    && sc.exe start PcieCubed.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/fd223833abffa9cd6cc1848d77599673643585925a7ee51259d67c44d361cce8.yara
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_mal_drivers_strict.yar
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
  url: https://www.mandiant.com/resources/blog/hunting-attestation-signed-malware
features:
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create PcieCubed.sys binPath=C:\\\\windows\\\\temp\\\\PcieCubed.sys type=kernel && sc.exe start PcieCubed.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver PcieCubed.sys"

# PcieCubed.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
