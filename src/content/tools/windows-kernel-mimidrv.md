---
id: windows-kernel-mimidrv
namespace: windows:kernel:mimidrv
name: "mimidrv.sys"
description: "Mimidrv is a signed Windows Driver Model WDM kernel mode software driver meant to be used with the standard Mimikatz executable."
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
  template: "sc.exe create mimidrv.sys binPath=C:\\windows\\temp\\mimidrv.sys type=kernel && sc.exe start mimidrv.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load mimidrv.sys kernel driver"
    commands:
      - "sc.exe create mimidrv.sys binPath=C:\\windows\\temp\\mimidrv.sys type=kernel && sc.exe start mimidrv.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/200f98655d1f46d2599c2c8605ebb7e335fee3883a32135ca1a81e09819bc64a.yara"
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
    url: "https://github.com/magicsword-io/LOLDrivers/issues/55#issuecomment-1537161951"
  - label: "Reference"
    url: "https://github.com/hfiref0x/KDU"
  - label: "Reference"
    url: "https://posts.specterops.io/mimidrv-in-depth-4d273d19e148"
  - label: "Reference"
    url: "https://github.com/gentilkiwi/mimikatz"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mimidrv.sys binPath=C:\\\\windows\\\\temp\\\\mimidrv.sys type=kernel && sc.exe start mimidrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver mimidrv.sys"

# mimidrv.sys

Mimidrv is a signed Windows Driver Model WDM kernel mode software driver meant to be used with the standard Mimikatz executable.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068