---
id: windows-kernel-zam64
namespace: windows:kernel:zam64
name: zam64.sys
description: Elevate privileges
author: Michael Haag, Nasreddine Bencherchali
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
  template: sc.exe create zam64.sys binPath=C:\windows\temp\zam64.sys type=kernel
    && sc.exe start zam64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load zam64.sys kernel driver
  commands:
  - sc.exe create zam64.sys binPath=C:\windows\temp\zam64.sys type=kernel && sc.exe
    start zam64.sys
detections:
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
  url: https://www.reddit.com/r/crowdstrike/comments/13wjrgn/20230531_situational_awareness_spyboy_defense/
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
- label: Reference
  url: https://www.trendmicro.com/en_us/research/23/e/attack-on-security-titans-earth-longzhi-returns-with-new-tricks.html
- label: Reference
  url: https://github.com/ZeroMemoryEx/Terminator
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create zam64.sys binPath=C:\\\\windows\\\\temp\\\\zam64.sys type=kernel && sc.exe start zam64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver zam64.sys"

# zam64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
