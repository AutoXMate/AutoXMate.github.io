---
id: windows-kernel-atszio
namespace: windows:kernel:atszio
name: ATSZIO.sys
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
  template: sc.exe create ATSZIO.sys binPath=C:\windows\temp\ATSZIO.sys type=kernel
    && sc.exe start ATSZIO.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ATSZIO.sys kernel driver
  commands:
  - sc.exe create ATSZIO.sys binPath=C:\windows\temp\ATSZIO.sys type=kernel && sc.exe
    start ATSZIO.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/01e024cb14b34b6d525c642a710bfa14497ea20fd287c39ba404b10a8b143ece.yara
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
  url: https://gist.github.com/k4nfr3/af970e7facb09195e56f2112e1c9549c
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ATSZIO.sys binPath=C:\\\\windows\\\\temp\\\\ATSZIO.sys type=kernel && sc.exe start ATSZIO.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ATSZIO.sys"

# ATSZIO.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
