---
id: windows-kernel-wantd
namespace: windows:kernel:wantd
name: wantd.sys
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
  template: sc.exe create wantd.sys binPath=C:\windows\temp\wantd.sys type=kernel
    && sc.exe start wantd.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load wantd.sys kernel driver
  commands:
  - sc.exe create wantd.sys binPath=C:\windows\temp\wantd.sys type=kernel && sc.exe
    start wantd.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/06a0ec9a316eb89cb041b1907918e3ad3b03842ec65f004f6fa74d57955573a4.yara
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
    command: "sc.exe create wantd.sys binPath=C:\\\\windows\\\\temp\\\\wantd.sys type=kernel && sc.exe start wantd.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wantd.sys"

# wantd.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
