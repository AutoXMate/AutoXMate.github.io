---
id: windows-kernel-physmem
namespace: windows:kernel:physmem
name: physmem.sys
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
  template: sc.exe create physmem.sys binPath=C:\windows\temp\physmem.sys type=kernel
    && sc.exe start physmem.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load physmem.sys kernel driver
  commands:
  - sc.exe create physmem.sys binPath=C:\windows\temp\physmem.sys type=kernel && sc.exe
    start physmem.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/c299063e3eae8ddc15839767e83b9808fd43418dc5a1af7e4f44b97ba53fbd3d.yara
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
  url: https://github.com/jbaines-r7/dellicious
- label: Reference
  url: https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/55
- label: Reference
  url: https://github.com/hfiref0x/KDU
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create physmem.sys binPath=C:\\\\windows\\\\temp\\\\physmem.sys type=kernel && sc.exe start physmem.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver physmem.sys"

# physmem.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
