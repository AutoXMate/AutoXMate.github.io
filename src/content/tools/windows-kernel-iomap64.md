---
id: windows-kernel-iomap64
namespace: windows:kernel:iomap64
name: IOMap64.sys
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
  template: sc.exe create IOMap64.sys binPath=C:\windows\temp\IOMap64.sys type=kernel
    && sc.exe start IOMap64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load IOMap64.sys kernel driver
  commands:
  - sc.exe create IOMap64.sys binPath=C:\windows\temp\IOMap64.sys type=kernel && sc.exe
    start IOMap64.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/ea85bbe63d6f66f7efee7007e770af820d57f914c7f179c5fee3ef2845f19c41.yara
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
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
- label: Reference
  url: https://www.asus.com/content/asus-product-security-advisory/
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create IOMap64.sys binPath=C:\\\\windows\\\\temp\\\\IOMap64.sys type=kernel && sc.exe start IOMap64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver IOMap64.sys"

# IOMap64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
