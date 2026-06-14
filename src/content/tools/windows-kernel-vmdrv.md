---
id: windows-kernel-vmdrv
namespace: windows:kernel:vmdrv
name: "vmdrv.sys"
description: "Elevate privileges"
author: "Nasreddine Bencherchali"
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
  template: "sc.exe create vmdrv.sys binPath=C:\\windows\\temp\\vmdrv.sys type=kernel && sc.exe start vmdrv.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load vmdrv.sys kernel driver"
    commands:
      - "sc.exe create vmdrv.sys binPath=C:\\windows\\temp\\vmdrv.sys type=kernel && sc.exe start vmdrv.sys"
detections:
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
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create vmdrv.sys binPath=C:\\\\windows\\\\temp\\\\vmdrv.sys type=kernel && sc.exe start vmdrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver vmdrv.sys"

# vmdrv.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants