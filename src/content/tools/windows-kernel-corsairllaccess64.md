---
id: windows-kernel-corsairllaccess64
namespace: windows:kernel:corsairllaccess64
name: "CorsairLLAccess64.sys"
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
  template: "sc.exe create CorsairLLAccess64.sys binPath=C:\\windows\\temp\\CorsairLLAccess64.sys type=kernel && sc.exe start CorsairLLAccess64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load CorsairLLAccess64.sys kernel driver"
    commands:
      - "sc.exe create CorsairLLAccess64.sys binPath=C:\\windows\\temp\\CorsairLLAccess64.sys type=kernel && sc.exe start CorsairLLAccess64.sys"
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
    command: "sc.exe create CorsairLLAccess64.sys binPath=C:\\\\windows\\\\temp\\\\CorsairLLAccess64.sys type=kernel && sc.exe start CorsairLLAccess64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CorsairLLAccess64.sys"

# CorsairLLAccess64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants