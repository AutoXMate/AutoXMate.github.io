---
id: windows-kernel-viragt64
namespace: windows:kernel:viragt64
name: "viragt64.sys"
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
  template: "sc.exe create viragt64.sys binPath=C:\\windows\\temp\\viragt64.sys type=kernel && sc.exe start viragt64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load viragt64.sys kernel driver"
    commands:
      - "sc.exe create viragt64.sys binPath=C:\\windows\\temp\\viragt64.sys type=kernel && sc.exe start viragt64.sys"
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
    command: "sc.exe create viragt64.sys binPath=C:\\\\windows\\\\temp\\\\viragt64.sys type=kernel && sc.exe start viragt64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver viragt64.sys"

# viragt64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068