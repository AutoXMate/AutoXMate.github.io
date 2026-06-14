---
id: windows-kernel-gdrv
namespace: windows:kernel:gdrv
name: "gdrv.sys"
description: "gdrv.sys is vulnerable to multiple CVEs: CVE-2018-19320, CVE-2018-19322, CVE-2018-19323, CVE-2018-19321. Read/Write Physical memory, read/write to/from IO ports, exposes ring0 memcpy-like functionality,  read and write Machine Specific Registers (MSRs). Affected versions: GIGABYTE APP Center v1.05.21 and previous, AORUS GRAPHICS ENGINE v1.33 and previous, XTREME GAMING ENGINE v1.25 and previous, OC GURU II v2.08"
author: "Michael Haag, rasta-mouse, goosvorbook"
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
  template: "sc.exe create gdrv.sys binPath=C:\\windows\\temp\\gdrv.sys type=kernel && sc.exe start gdrv.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load gdrv.sys kernel driver"
    commands:
      - "sc.exe create gdrv.sys binPath=C:\\windows\\temp\\gdrv.sys type=kernel && sc.exe start gdrv.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/31f4cfb4c71da44120752721103a16512444c13c2ac2d857a7e6f13cb679b427.yara"
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/ff6729518a380bf57f1bc6f1ec0aa7f3012e1618b8d9b0f31a61d299ee2b4339.yara"
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
    url: "https://github.com/hoangprod/DanSpecial"
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
  - label: "Reference"
    url: "https://www.secureauth.com/labs/advisories/gigabyte-drivers-elevation-privilege-vulnerabilities"
  - label: "Reference"
    url: "https://medium.com/@fsx30/weaponizing-vulnerable-driver-for-privilege-escalation-gigabyte-edition-e73ee523598b"
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
  - label: "Reference"
    url: "https://github.com/hmnthabit/CVE-2018-19320-LPE"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create gdrv.sys binPath=C:\\\\windows\\\\temp\\\\gdrv.sys type=kernel && sc.exe start gdrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver gdrv.sys"

# gdrv.sys

gdrv.sys is vulnerable to multiple CVEs: CVE-2018-19320, CVE-2018-19322, CVE-2018-19323, CVE-2018-19321. Read/Write Physical memory, read/write to/from IO ports, exposes ring0 memcpy-like functionality,  read and write Machine Specific Registers (MSRs). Affected versions: GIGABYTE APP Center v1.05.21 and previous, AORUS GRAPHICS ENGINE v1.33 and previous, XTREME GAMING ENGINE v1.25 and previous, OC GURU II v2.08

**Use Case:** Elevate privileges, tamper with PPL or system processes

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants