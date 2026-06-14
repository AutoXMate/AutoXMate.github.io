---
id: windows-kernel-bs-rcio64
namespace: windows:kernel:bs-rcio64
name: "BS_RCIO64.sys"
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
  template: "sc.exe create BS_RCIO64.sys binPath=C:\\windows\\temp\\BS_RCIO64.sys type=kernel && sc.exe start BS_RCIO64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load BS_RCIO64.sys kernel driver"
    commands:
      - "sc.exe create BS_RCIO64.sys binPath=C:\\windows\\temp\\BS_RCIO64.sys type=kernel && sc.exe start BS_RCIO64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/d205286bffdf09bc033c09e95c519c1c267b40c2ee8bab703c6a2d86741ccd3e.yara"
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
    url: "https://github.com/jbaines-r7/dellicious"
  - label: "Reference"
    url: "https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/"
  - label: "Reference"
    url: "https://github.com/elastic/protections-artifacts/blob/932baf346cc8a743f1963ad3d4565b42ed17bebe/yara/rules/Windows_VulnDriver_Biostar.yar#L54"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BS_RCIO64.sys binPath=C:\\\\windows\\\\temp\\\\BS_RCIO64.sys type=kernel && sc.exe start BS_RCIO64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BS_RCIO64.sys"

# BS_RCIO64.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068