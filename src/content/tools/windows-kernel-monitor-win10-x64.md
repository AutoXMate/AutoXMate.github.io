---
id: windows-kernel-monitor-win10-x64
namespace: windows:kernel:monitor-win10-x64
name: Monitor_win10_x64.sys
description: CVE-2018-16712
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
  template: sc.exe create Monitor_win10_x64.sys binPath=C:\windows\temp\Monitor_win10_x64.sys     type=kernel
    && sc.exe start Monitor_win10_x64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Monitor_win10_x64.sys kernel driver
  commands:
  - sc.exe create Monitor_win10_x64.sys binPath=C:\windows\temp\Monitor_win10_x64.sys     type=kernel
    && sc.exe start Monitor_win10_x64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/e4a7da2cf59a4a21fc42b611df1d59cae75051925a7ddf42bf216cc1a026eadb.yara
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
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
features:
- requires-root
- streaming
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Monitor_win10_x64.sys binPath=C:\\\\windows\\\\temp\\\\Monitor_win10_x64.sys     type=kernel && sc.exe start Monitor_win10_x64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Monitor_win10_x64.sys"

# Monitor_win10_x64.sys

CVE-2018-16712

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
