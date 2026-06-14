---
id: windows-kernel-gtckmdfbs
namespace: windows:kernel:gtckmdfbs
name: "GtcKmdfBs.sys"
description: "The Carbon Black Threat Analysis Unit (TAU) discovered 34 unique vulnerable drivers (237 file hashes) accepting firmware access. Six allow kernel memory access. All give full control of the devices to non-admin users. By exploiting the vulnerable drivers, an attacker without the system privilege may erase/alter firmware, and/or elevate privileges. As of the time of writing in October 2023, the filenames of the vulnerable drivers have not been made public until now."
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
  template: "sc.exe create GtcKmdfBssys binPath= C:\\windows\\temp\\GtcKmdfBssys.sys type=kernel && sc.exe start GtcKmdfBssys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load GtcKmdfBs.sys kernel driver"
    commands:
      - "sc.exe create GtcKmdfBssys binPath= C:\\windows\\temp\\GtcKmdfBssys.sys type=kernel && sc.exe start GtcKmdfBssys"
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
    url: "https://blogs.vmware.com/security/2023/10/hunting-vulnerable-kernel-drivers.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create GtcKmdfBssys binPath= C:\\\\windows\\\\temp\\\\GtcKmdfBssys.sys type=kernel && sc.exe start GtcKmdfBssys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver GtcKmdfBs.sys"

# GtcKmdfBs.sys

The Carbon Black Threat Analysis Unit (TAU) discovered 34 unique vulnerable drivers (237 file hashes) accepting firmware access. Six allow kernel memory access. All give full control of the devices to non-admin users. By exploiting the vulnerable drivers, an attacker without the system privilege may erase/alter firmware, and/or elevate privileges. As of the time of writing in October 2023, the filenames of the vulnerable drivers have not been made public until now.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068