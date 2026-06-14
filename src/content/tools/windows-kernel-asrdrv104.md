---
id: windows-kernel-asrdrv104
namespace: windows:kernel:asrdrv104
name: "asrdrv104.sys"
description: "Elevate privileges"
author: "Michael Haag"
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
  template: "sc.exe create asrdrv104.sys binPath=C:\\windows\\temp\\asrdrv104.sys type=kernel && sc.exe start asrdrv104.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load asrdrv104.sys kernel driver"
    commands:
      - "sc.exe create asrdrv104.sys binPath=C:\\windows\\temp\\asrdrv104.sys type=kernel && sc.exe start asrdrv104.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/6ed35f310c96920a271c59a097b382da07856e40179c2a4239f8daa04eef38e7.yara"
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
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create asrdrv104.sys binPath=C:\\\\windows\\\\temp\\\\asrdrv104.sys type=kernel && sc.exe start asrdrv104.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver asrdrv104.sys"

# asrdrv104.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068