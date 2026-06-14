---
id: windows-kernel-wantd-6
namespace: windows:kernel:wantd-6
name: wantd_6.sys
description: Driver used in the Daxin malware campaign.
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
  template: sc.exe create wantd_6.sys binPath=C:\windows\temp\wantd_6.sys type=kernel
    && sc.exe start wantd_6.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load wantd_6.sys kernel driver
  commands:
  - sc.exe create wantd_6.sys binPath=C:\windows\temp\wantd_6.sys type=kernel && sc.exe
    start wantd_6.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/e7af7bcb86bd6bab1835f610671c3921441965a839673ac34444cf0ce7b2164e.yara
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
  url: https://gist.github.com/MHaggis/9ab3bb795a6018d70fb11fa7c31f8f48
- label: Reference
  url: https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/daxin-backdoor-espionage
features:
- pipes-stdin
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create wantd_6.sys binPath=C:\\\\windows\\\\temp\\\\wantd_6.sys type=kernel && sc.exe start wantd_6.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wantd_6.sys"

# wantd_6.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
