---
id: windows-kernel-dbutildrv2
namespace: windows:kernel:dbutildrv2
name: DBUtilDrv2.sys
description: Dell DBUtilDrv2.sys versions 2.5, 2.6, and 2.7 all contain a write-what-where
  condition allowing kernel memory read/write. Dell released v2.7 as a remediation
  for CVE-2021-36276 but the fix was incomplete. Rapid7 confirmed v2.7 retains the
  kernel memory primitive and published the dellicious PoC and a Metasploit module
  (post/windows/manage/dell_memory_protect) that works against both v2.5 and v2.7.
  Dell categorized the v2.7 issue as a weakness rather than a vulnerability, stating
  it requires ...
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
  template: sc.exe create DBUtilDrv2.sys binPath=C:\windows\temp\DBUtilDrv2.sys type=kernel
    && sc.exe start DBUtilDrv2.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load DBUtilDrv2.sys kernel driver
  commands:
  - sc.exe create DBUtilDrv2.sys binPath=C:\windows\temp\DBUtilDrv2.sys type=kernel
    && sc.exe start DBUtilDrv2.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/71fe5af0f1564dc187eea8d59c0fbc897712afa07d18316d2080330ba17cf009.yara
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
  url: https://www.bleepingcomputer.com/news/security/dell-driver-fix-still-allows-windows-kernel-level-attacks/
- label: Reference
  url: https://www.rapid7.com/db/modules/post/windows/manage/dell_memory_protect/
features:
- file-system
- pipes-stdin
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create DBUtilDrv2.sys binPath=C:\\\\windows\\\\temp\\\\DBUtilDrv2.sys type=kernel && sc.exe start DBUtilDrv2.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver DBUtilDrv2.sys"

# DBUtilDrv2.sys

Dell DBUtilDrv2.sys versions 2.5, 2.6, and 2.7 all contain a write-what-where condition allowing kernel memory read/write. Dell released v2.7 as a remediation for CVE-2021-36276 but the fix was incomplete. Rapid7 confirmed v2.7 retains the kernel memory primitive and published the dellicious PoC and a Metasploit module (post/windows/manage/dell_memory_protect) that works against both v2.5 and v2.7. Dell categorized the v2.7 issue as a weakness rather than a vulnerability, stating it requires admin privileges.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
