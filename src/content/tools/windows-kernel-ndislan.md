---
id: windows-kernel-ndislan
namespace: windows:kernel:ndislan
name: ndislan.sys
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
  template: sc.exe create ndislan.sys binPath=C:\windows\temp \n \n \n  dislan.sys
    type=kernel && sc.exe start ndislan.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ndislan.sys kernel driver
  commands:
  - sc.exe create ndislan.sys binPath=C:\windows\temp \n \n \n  dislan.sys type=kernel
    && sc.exe start ndislan.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/b0eb4d999e4e0e7c2e33ff081e847c87b49940eb24a9e0794c6aa9516832c427.yara
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
    command: "sc.exe create ndislan.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  dislan.sys type=kernel && sc.exe start ndislan.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ndislan.sys"

# ndislan.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
