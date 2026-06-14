---
id: windows-kernel-wantd-2
namespace: windows:kernel:wantd-2
name: wantd_2.sys
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
  template: sc.exe create wantd_2.sys binPath=C:\windows\temp\wantd_2.sys type=kernel
    && sc.exe start wantd_2.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load wantd_2.sys kernel driver
  commands:
  - sc.exe create wantd_2.sys binPath=C:\windows\temp\wantd_2.sys type=kernel && sc.exe
    start wantd_2.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/6908ebf52eb19c6719a0b508d1e2128f198d10441551cbfb9f4031d382f5229f.yara
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
    command: "sc.exe create wantd_2.sys binPath=C:\\\\windows\\\\temp\\\\wantd_2.sys type=kernel && sc.exe start wantd_2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wantd_2.sys"

# wantd_2.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
