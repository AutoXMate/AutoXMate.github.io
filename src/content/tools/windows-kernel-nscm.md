---
id: windows-kernel-nscm
namespace: windows:kernel:nscm
name: "nscm.sys"
description: "nscm.sys is a vulnerable driver. CVE-2013-3956."
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
  template: "sc.exe create nscm.sys binPath=C:\\windows\\temp \\n \\n \\n  scm.sys type=kernel && sc.exe start nscm.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load nscm.sys kernel driver"
    commands:
      - "sc.exe create nscm.sys binPath=C:\\windows\\temp \\n \\n \\n  scm.sys type=kernel && sc.exe start nscm.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/76660e91f1ff3cb89630df5af4fe09de6098d09baa66b1a130c89c3c5edd5b22.yara"
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
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nscm.sys binPath=C:\\\\windows\\\\temp \\\\n \\\\n \\\\n  scm.sys type=kernel && sc.exe start nscm.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nscm.sys"

# nscm.sys

nscm.sys is a vulnerable driver. CVE-2013-3956.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants