---
id: windows-kernel-dh-kernel
namespace: windows:kernel:dh-kernel
name: "Dh_Kernel.sys"
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
trust_level: verified
execution:
  template: "sc.exe create Dh_Kernel.sys binPath=C:\\windows\\temp\\Dh_Kernel.sys type=kernel && sc.exe start Dh_Kernel.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load Dh_Kernel.sys kernel driver"
    commands:
      - "sc.exe create Dh_Kernel.sys binPath=C:\\windows\\temp\\Dh_Kernel.sys type=kernel && sc.exe start Dh_Kernel.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/bb50818a07b0eb1bd317467139b7eb4bad6cd89053fecdabfeae111689825955.yara"
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
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Dh_Kernel.sys binPath=C:\\\\windows\\\\temp\\\\Dh_Kernel.sys type=kernel && sc.exe start Dh_Kernel.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Dh_Kernel.sys"

# Dh_Kernel.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068