---
id: windows-kernel-bs-def64
namespace: windows:kernel:bs-def64
name: BS_Def64.sys
description: Elevate privileges
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: sc.exe create BS_Def64.sys binPath=C:\windows\temp\BS_Def64.sys type=kernel
    && sc.exe start BS_Def64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BS_Def64.sys kernel driver
  commands:
  - sc.exe create BS_Def64.sys binPath=C:\windows\temp\BS_Def64.sys type=kernel &&
    sc.exe start BS_Def64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/0040153302b88bee27eb4f1eca6855039e1a057370f5e8c615724fa5215bada3.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/3326e2d32bbabd69feb6024809afc56c7e39241ebe70a53728c77e80995422a5.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/36b9e31240ab0341873c7092b63e2e0f2cab2962ebf9b25271c3a1216b7669eb.yara
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict_renamed.yar
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml
- type: sigma
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml
- type: sysmon
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml
references:
- label: Reference
  url: https://github.com/namazso/physmem_drivers
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_Def64.sys binPath=C:\\\\windows\\\\temp\\\\BS_Def64.sys type=kernel && sc.exe start BS_Def64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_Def64.sys"

# BS_Def64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
