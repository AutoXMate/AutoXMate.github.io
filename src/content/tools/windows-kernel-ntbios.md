---
id: windows-kernel-ntbios
namespace: windows:kernel:ntbios
name: "ntbios.sys"
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
  template: "sc.exe create ntbios.sys binPath=C:\\windows\\temp \\n \\n \\n  tbios.sys type=kernel && sc.exe start ntbios.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ntbios.sys kernel driver"
    commands:
      - "sc.exe create ntbios.sys binPath=C:\\windows\\temp \\n \\n \\n  tbios.sys type=kernel && sc.exe start ntbios.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/96bf3ee7c6673b69c6aa173bb44e21fa636b1c2c73f4356a7599c121284a51cc.yara"
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
    command: "sc.exe create ntbios.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  tbios.sys type=kernel && sc.exe start ntbios.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ntbios.sys"

# ntbios.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068