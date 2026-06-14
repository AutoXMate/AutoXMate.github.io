---
id: windows-kernel-wantd-3
namespace: windows:kernel:wantd-3
name: "wantd_3.sys"
description: "Driver used in the Daxin malware campaign."
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: "sc.exe create wantd_3.sys binPath=C:\\windows\\temp\\wantd_3.sys type=kernel && sc.exe start wantd_3.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load wantd_3.sys kernel driver"
    commands:
      - "sc.exe create wantd_3.sys binPath=C:\\windows\\temp\\wantd_3.sys type=kernel && sc.exe start wantd_3.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/81c7bb39100d358f8286da5e9aa838606c98dfcc263e9a82ed91cd438cb130d1.yara"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_mal_drivers_strict.yar"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
references:
  - label: "Reference"
    url: "https://gist.github.com/MHaggis/9ab3bb795a6018d70fb11fa7c31f8f48"
  - label: "Reference"
    url: "https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/daxin-backdoor-espionage"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create wantd_3.sys binPath=C:\\\\windows\\\\temp\\\\wantd_3.sys type=kernel && sc.exe start wantd_3.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wantd_3.sys"

# wantd_3.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068