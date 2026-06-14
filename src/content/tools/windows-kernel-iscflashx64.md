---
id: windows-kernel-iscflashx64
namespace: windows:kernel:iscflashx64
name: "iscflashx64.sys"
description: "CVE-2021-33834"
author: "Takahiro Haruyama"
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
  template: "sc.exe create iscflashx64.sys binPath=C:\\windows\\temp\\iscflashx64.sys type=kernel && sc.exe start iscflashx64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load iscflashx64.sys kernel driver"
    commands:
      - "sc.exe create iscflashx64.sys binPath=C:\\windows\\temp\\iscflashx64.sys type=kernel && sc.exe start iscflashx64.sys"
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
    command: "sc.exe create iscflashx64.sys binPath=C:\\\\windows\\\\temp\\\\iscflashx64.sys type=kernel && sc.exe start iscflashx64.sys"

# iscflashx64.sys

CVE-2021-33834

**Use Case:** firmware erasing/modification

**Required Privileges:** kernel

**MITRE ATT&CK:** T1542