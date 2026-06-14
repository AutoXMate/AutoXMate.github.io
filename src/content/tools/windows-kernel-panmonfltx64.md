---
id: windows-kernel-panmonfltx64
namespace: windows:kernel:panmonfltx64
name: "PanMonFltX64.sys"
description: "Elevate privileges"
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: community
execution:
  template: "sc.exe create PanMonFltX64.sys binPath=C:\\windows\\temp\\PanMonFltX64.sys     type=kernel && sc.exe start PanMonFltX64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load PanMonFltX64.sys kernel driver"
    commands:
      - "sc.exe create PanMonFltX64.sys binPath=C:\\windows\\temp\\PanMonFltX64.sys     type=kernel && sc.exe start PanMonFltX64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/06508aacb4ed0a1398a2b0da5fa2dbf7da435b56da76fd83c759a50a51c75caf.yara"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict_renamed.yar"
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
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create PanMonFltX64.sys binPath=C:\\\\windows\\\\temp\\\\PanMonFltX64.sys     type=kernel && sc.exe start PanMonFltX64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver PanMonFltX64.sys"

# PanMonFltX64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068