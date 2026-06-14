---
id: windows-kernel-asmio64
namespace: windows:kernel:asmio64
name: "AsmIo64.sys"
description: "Elevate privileges, firmware erasing/modification"
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
  template: "sc.exe create AsmIo64.sys binPath=C:\\windows\\temp\\AsmIo64.sys type=kernel && sc.exe start AsmIo64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load AsmIo64.sys kernel driver"
    commands:
      - "sc.exe create AsmIo64.sys binPath=C:\\windows\\temp\\AsmIo64.sys type=kernel && sc.exe start AsmIo64.sys"
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
    url: "https://github.com/ucsb-seclab/popkorn-artifact/tree/main/evaluation"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsmIo64.sys binPath=C:\\\\windows\\\\temp\\\\AsmIo64.sys type=kernel && sc.exe start AsmIo64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsmIo64.sys"

# AsmIo64.sys

**Use Case:** Elevate privileges, firmware erasing/modification

**Required Privileges:** kernel

**MITRE ATT&CK:** T1542, T1068