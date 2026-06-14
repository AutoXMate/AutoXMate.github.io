---
id: windows-kernel-lenovodiagnosticsdriver
namespace: windows:kernel:lenovodiagnosticsdriver
name: LenovoDiagnosticsDriver.sys
description: The aforementioned driver has been identified as vulnerable to CVE-2022-3699
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
  template: sc.exe create LenovoDiagnosticsDriver.sys binPath=C:\windows\temp\LenovoDiagnosticsDriver.sys
    type=kernel && sc.exe start LenovoDiagnosticsDriver.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load LenovoDiagnosticsDriver.sys kernel driver
  commands:
  - sc.exe create LenovoDiagnosticsDriver.sys binPath=C:\windows\temp\LenovoDiagnosticsDriver.sys
    type=kernel && sc.exe start LenovoDiagnosticsDriver.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/f05b1ee9e2f6ab704b8919d5071becbce6f9d0f9d0ba32a460c41d5272134abe.yara
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
  url: https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
- label: Reference
  url: https://nephosec.com/cve-2022-3699-lenovo-diagnostics-driver-eop-arbitrary-r-w/
- label: Reference
  url: https://github.com/alfarom256/CVE-2022-3699
- label: Reference
  url: https://support.lenovo.com/us/en/product_security/LEN-94532
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create LenovoDiagnosticsDriver.sys binPath=C:\\\\windows\\\\temp\\\\LenovoDiagnosticsDriver.sys type=kernel && sc.exe start LenovoDiagnosticsDriver.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver LenovoDiagnosticsDriver.sys"

# LenovoDiagnosticsDriver.sys

The aforementioned driver has been identified as vulnerable to CVE-2022-3699

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
