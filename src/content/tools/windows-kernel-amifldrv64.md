---
id: windows-kernel-amifldrv64
namespace: windows:kernel:amifldrv64
name: "amifldrv64.sys"
description: "Elevate privileges"
author: "Michael Haag, Nasreddine Bencherchali"
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
  template: "sc.exe create amifldrv64.sys binPath=C:\\windows\\temp\\amifldrv64.sys type=kernel && sc.exe start amifldrv64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load amifldrv64.sys kernel driver"
    commands:
      - "sc.exe create amifldrv64.sys binPath=C:\\windows\\temp\\amifldrv64.sys type=kernel && sc.exe start amifldrv64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/38d87b51f4b69ba2dae1477684a1415f1a3b578eee5e1126673b1beaefee9a20.yara"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/ffc72f0bde21ba20aa97bee99d9e96870e5aa40cce9884e44c612757f939494f.yara"
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
    url: "https://github.com/namazso/physmem_drivers"
  - label: "Reference"
    url: "https://gist.github.com/mgraeber-rc/1bde6a2a83237f17b463d051d32e802c"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create amifldrv64.sys binPath=C:\\\\windows\\\\temp\\\\amifldrv64.sys type=kernel && sc.exe start amifldrv64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver amifldrv64.sys"

# amifldrv64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068