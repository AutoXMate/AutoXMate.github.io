---
id: windows-kernel-adv64drv
namespace: windows:kernel:adv64drv
name: "ADV64DRV.sys"
description: "Elevate privileges"
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: verified
execution:
  template: "sc.exe create ADV64DRV.sys binPath=C:\\windows\\temp\\ADV64DRV.sys type=kernel && sc.exe start ADV64DRV.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ADV64DRV.sys kernel driver"
    commands:
      - "sc.exe create ADV64DRV.sys binPath=C:\\windows\\temp\\ADV64DRV.sys type=kernel && sc.exe start ADV64DRV.sys"
detections:
  - type: other
    url: "https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules"
  - type: other
    description: "Utilize Windows Event Code 7045 to monitor for new kernel driver installation."
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/04a85e359525d662338cae86c1e59b1d7aa9bd12b920e8067503723dc1e03162.yara"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/yara-rules_vuln_drivers_strict_renamed.yar"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers.yml"
  - type: sigma
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sigma/driver_load_win_vuln_drivers_names.yml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes.xml"
  - type: sysmon
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/sysmon/sysmon_config_vulnerable_hashes_block.xml"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ADV64DRV.sys binPath=C:\\\\windows\\\\temp\\\\ADV64DRV.sys type=kernel && sc.exe start ADV64DRV.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ADV64DRV.sys"

# ADV64DRV.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068