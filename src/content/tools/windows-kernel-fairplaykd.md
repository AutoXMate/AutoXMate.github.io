---
id: windows-kernel-fairplaykd
namespace: windows:kernel:fairplaykd
name: FairplayKD.sys
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
trust_level: community
execution:
  template: sc.exe create FairplayKD.sys binPath=C:\windows\temp\FairplayKD.sys type=kernel
    && sc.exe start FairplayKD.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load FairplayKD.sys kernel driver
  commands:
  - sc.exe create FairplayKD.sys binPath=C:\windows\temp\FairplayKD.sys type=kernel
    && sc.exe start FairplayKD.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/9f4ce6ab5e8d44f355426d9a6ab79833709f39b300733b5b251a0766e895e0e5.yara
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
  url: https://www.unknowncheats.me/forum/anti-cheat-bypass/334557-vulnerable-driver-megathread.html
- label: Reference
  url: https://www.unknowncheats.me/forum/anti-cheat-bypass/244386-mta-fairplaykd-driver-reversed-exploited-rpm.html
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create FairplayKD.sys binPath=C:\\\\windows\\\\temp\\\\FairplayKD.sys type=kernel && sc.exe start FairplayKD.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver FairplayKD.sys"

# FairplayKD.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
