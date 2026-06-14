---
id: windows-kernel-lgcoretemp
namespace: windows:kernel:lgcoretemp
name: "LgCoreTemp.sys"
description: "Denial of Service"
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
  template: "sc.exe create LgCoreTemp.sys binPath=C:\\windows\\temp\\LgCoreTemp.sys     type=kernel && sc.exe start LgCoreTemp.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load LgCoreTemp.sys kernel driver"
    commands:
      - "sc.exe create LgCoreTemp.sys binPath=C:\\windows\\temp\\LgCoreTemp.sys     type=kernel && sc.exe start LgCoreTemp.sys"
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
references:
  - label: "Reference"
    url: "https://github.com/VoidSec/Exploit-Development/tree/b82b6d3ac1cce66221101d3e0f4634aa64cb4ca7/windows/x64/kernel/logitech_v.9.02.65_DoS"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create LgCoreTemp.sys binPath=C:\\\\windows\\\\temp\\\\LgCoreTemp.sys     type=kernel && sc.exe start LgCoreTemp.sys"

# LgCoreTemp.sys

**Use Case:** Denial of Service

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068