---
id: windows-kernel-kprocesshacker
namespace: windows:kernel:kprocesshacker
name: kprocesshacker.sys
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
  template: sc.exe create krpocesshacker.sys binPath=C:\windows\temp\krpocesshacker.sys     type=kernel
    && sc.exe start krpocesshacker.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load kprocesshacker.sys kernel driver
  commands:
  - sc.exe create krpocesshacker.sys binPath=C:\windows\temp\krpocesshacker.sys     type=kernel
    && sc.exe start krpocesshacker.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/c725919e6357126d512c638f993cf572112f323da359645e4088f789eb4c7b8c.yara
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
  url: https://www.unknowncheats.me/forum/anti-cheat-bypass/312791-bypaph-process-hackers-bypass-read-write-process-virtual-memory-kernel-mem.html#post2315763
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
features:
- network-intensive
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create krpocesshacker.sys binPath=C:\\\\windows\\\\temp\\\\krpocesshacker.sys     type=kernel && sc.exe start krpocesshacker.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver kprocesshacker.sys"

# kprocesshacker.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
