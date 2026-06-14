---
id: windows-kernel-nseckrnl
namespace: windows:kernel:nseckrnl
name: "NSecKrnl.sys"
description: "Driver used by ValleyRAT malware to terminate security processes via IOCTL 0x2248E0"
author: "Michael Haag"
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
  template: "sc.exe create NSecKrnl binPath=C:\\windows\\temp\\NSecKrnl.sys type=kernel && sc.exe start NSecKrnl"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load NSecKrnl.sys kernel driver"
    commands:
      - "sc.exe create NSecKrnl binPath=C:\\windows\\temp\\NSecKrnl.sys type=kernel && sc.exe start NSecKrnl"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict.yar"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
references:
  - label: "Reference"
    url: "https://hexastrike.com/resources/blog/threat-intelligence/valleyrat-exploiting-byovd-to-kill-endpoint-security/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NSecKrnl binPath=C:\\\\windows\\\\temp\\\\NSecKrnl.sys type=kernel && sc.exe start NSecKrnl"

# NSecKrnl.sys

Driver used by ValleyRAT malware to terminate security processes via IOCTL 0x2248E0

**Use Case:** Terminate security processes

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068