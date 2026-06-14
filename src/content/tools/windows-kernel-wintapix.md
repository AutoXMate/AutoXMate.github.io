---
id: windows-kernel-wintapix
namespace: windows:kernel:wintapix
name: "WinTapix.sys"
description: "Wintapix.sys is partially protected by VMProtect, a software protection tool that uses virtualization to protect software applications from reverse engineering and unauthorized usage. It transforms the original executable file into a virtualized code executed in a protected environment, making it difficult to analyze and tamper with."
author: "Guus Verbeek"
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
  template: "sc.exe create WinTapix.sys binPath=C:\\windows\\temp\\WinTapix.sys type=kernel && sc.exe start WinTapix.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load WinTapix.sys kernel driver"
    commands:
      - "sc.exe create WinTapix.sys binPath=C:\\windows\\temp\\WinTapix.sys type=kernel && sc.exe start WinTapix.sys"
detections:
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
    url: "https://www.fortinet.com/blog/threat-research/wintapix-kernal-driver-middle-east-countries"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinTapix.sys binPath=C:\\\\windows\\\\temp\\\\WinTapix.sys type=kernel && sc.exe start WinTapix.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinTapix.sys"

# WinTapix.sys

Wintapix.sys is partially protected by VMProtect, a software protection tool that uses virtualization to protect software applications from reverse engineering and unauthorized usage. It transforms the original executable file into a virtualized code executed in a protected environment, making it difficult to analyze and tamper with.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068