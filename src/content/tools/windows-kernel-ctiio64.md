---
id: windows-kernel-ctiio64
namespace: windows:kernel:ctiio64
name: "CtiIo64.sys"
description: "The driver is part of Dragon Center (or MSI Center?) from MSI. It creates \\Device\\CtiIo ACLless DO and provides access to memory and IO. The driver is signed with WHQL cert."
author: "zwclose"
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
  template: "sc.exe create CtiIo64.sys binPath=C:\\windows\\temp\\CtiIo64.sys type=kernel && sc.exe start CtiIo64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load CtiIo64.sys kernel driver"
    commands:
      - "sc.exe create CtiIo64.sys binPath=C:\\windows\\temp\\CtiIo64.sys type=kernel && sc.exe start CtiIo64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/2121a2bb8ebbf2e6e82c782b6f3c6b7904f686aa495def25cf1cf52a42e16109.yara"
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
    url: "https://github.com/magicsword-io/LOLDrivers/pull/81"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CtiIo64.sys binPath=C:\\\\windows\\\\temp\\\\CtiIo64.sys type=kernel && sc.exe start CtiIo64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CtiIo64.sys"

# CtiIo64.sys

The driver is part of Dragon Center (or MSI Center?) from MSI. It creates \Device\CtiIo ACLless DO and provides access to memory and IO. The driver is signed with WHQL cert.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068