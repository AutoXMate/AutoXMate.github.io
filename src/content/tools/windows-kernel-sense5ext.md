---
id: windows-kernel-sense5ext
namespace: windows:kernel:sense5ext
name: Sense5Ext.sys
description: Driver categorized as POORTRY by Mandiant.
author: Michael Haag, Guus Verbeek
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
  template: sc.exe create Sense5Ext.sys binPath=C:\windows\temp\Sense5Ext.sys type=kernel
    && sc.exe start Sense5Ext.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Sense5Ext.sys kernel driver
  commands:
  - sc.exe create Sense5Ext.sys binPath=C:\windows\temp\Sense5Ext.sys type=kernel
    && sc.exe start Sense5Ext.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/7f4555a940ce1156c9bcea9a2a0b801f9a5e44ec9400b61b14a7b1a6404ffdf6.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/42b22faa489b5de936db33f12184f6233198bdf851a18264d31210207827ba25.yara
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
    command: "sc.exe create Sense5Ext.sys binPath=C:\\\\windows\\\\temp\\\\Sense5Ext.sys type=kernel && sc.exe start Sense5Ext.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Sense5Ext.sys"

# Sense5Ext.sys

Driver categorized as POORTRY by Mandiant.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
