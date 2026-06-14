---
id: windows-kernel-ntbios-2
namespace: windows:kernel:ntbios-2
name: "ntbios_2.sys"
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
  template: "sc.exe create ntbios_2.sys binPath=C:\\windows\\temp \\n \\n \\n  tbios_2.sys type=kernel && sc.exe start ntbios_2.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ntbios_2.sys kernel driver"
    commands:
      - "sc.exe create ntbios_2.sys binPath=C:\\windows\\temp \\n \\n \\n  tbios_2.sys type=kernel && sc.exe start ntbios_2.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/c0d88db11d0f529754d290ed5f4c34b4dba8c4f2e5c4148866daabeab0d25f9c.yara"
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
    command: "sc.exe create ntbios_2.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  tbios_2.sys type=kernel && sc.exe start ntbios_2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ntbios_2.sys"

# ntbios_2.sys

Driver used in the Daxin malware campaign.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068