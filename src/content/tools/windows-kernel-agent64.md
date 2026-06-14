---
id: windows-kernel-agent64
namespace: windows:kernel:agent64
name: Agent64.sys
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
  template: sc.exe create Agent64.sys binPath=C:\windows\temp\Agent64.sys type=kernel
    && sc.exe start Agent64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Agent64.sys kernel driver
  commands:
  - sc.exe create Agent64.sys binPath=C:\windows\temp\Agent64.sys type=kernel && sc.exe
    start Agent64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/05f052c64d192cf69a462a5ec16dda0d43ca5d0245900c9fcb9201685a2e7748.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/4045ae77859b1dbf13972451972eaaf6f3c97bea423e9e78f1c2f14330cd47ca.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/6948480954137987a0be626c24cf594390960242cd75f094cd6aaa5c2e7a54fa.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/8cb62c5d41148de416014f80bd1fd033fd4d2bd504cb05b90eeb6992a382d58f.yara
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/b1d96233235a62dbb21b8dbe2d1ae333199669f67664b107bff1ad49b41d9414.yara
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
    command: "sc.exe create Agent64.sys binPath=C:\\\\windows\\\\temp\\\\Agent64.sys type=kernel && sc.exe start Agent64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Agent64.sys"

# Agent64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
