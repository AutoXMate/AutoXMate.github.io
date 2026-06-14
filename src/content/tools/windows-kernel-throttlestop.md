---
id: windows-kernel-throttlestop
namespace: windows:kernel:throttlestop
name: "throttlestop.sys"
description: "ThrottleStop is developed by TechPowerUp and is designed to monitor for and correct CPU throttling issues. However, Kaspersky researchers from the Global Emergency Response Team (GERT) found out that it is being abused by attackers to terminate defense mechanisms."
author: "Cristian Souza"
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
  template: "sc.exe create throttlestop.sys binPath= C:\\windows\\temp\\throttlestop.sys type=kernel && sc.exe start throttlestop.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load throttlestop.sys kernel driver"
    commands:
      - "sc.exe create throttlestop.sys binPath= C:\\windows\\temp\\throttlestop.sys type=kernel && sc.exe start throttlestop.sys"
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
    url: "https://securelist.com/av-killer-exploiting-throttlestop-sys/117026/"
  - label: "Reference"
    url: "https://www.cve.org/CVERecord?id=CVE-2025-7771"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create throttlestop.sys binPath= C:\\\\windows\\\\temp\\\\throttlestop.sys type=kernel && sc.exe start throttlestop.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver throttlestop.sys"

# throttlestop.sys

ThrottleStop is developed by TechPowerUp and is designed to monitor for and correct CPU throttling issues. However, Kaspersky researchers from the Global Emergency Response Team (GERT) found out that it is being abused by attackers to terminate defense mechanisms.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068