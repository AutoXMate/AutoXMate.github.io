---
id: windows-kernel-kfeco11x64
namespace: windows:kernel:kfeco11x64
name: "KfeCo11X64.sys"
description: "Killer exposes COM interfaces that allow non-privileged users 1) to block network for any process 2) to manage any service in the OS. Killer is preinstalled to laptops equipped with Intel Killer NICs (e.g. Dell). Since Intel patched the vulnerability quietly, it's not clear which version is safe. Also, it is unclear which OEMs are affected. Dell is definitely in the list, but it is likely that other vendors with Killer NICs on board, such as Acer and MSI, are affected too. Some users think th..."
author: "Paul Michaud"
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
  template: "sc.exe create KfeCo11X64.sys binPath=C:\\windows\\temp\\KfeCo11X64.sys type=kernel && sc.exe start KfeCo11X64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load KfeCo11X64.sys kernel driver"
    commands:
      - "sc.exe create KfeCo11X64.sys binPath=C:\\windows\\temp\\KfeCo11X64.sys type=kernel && sc.exe start KfeCo11X64.sys"
detections:
  - type: yara
    url: "https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/9a91d6e83b8fdec536580f6617f10dfc64eedf14ead29a6a644eb154426622ba.yara"
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
    url: "https://zwclose.github.io/2023/04/18/killer2.html"
  - label: "Reference"
    url: "https://twitter.com/zwclose/status/1648441215808049153"
  - label: "Reference"
    url: "https://zwclose.github.io/2022/12/18/killer1.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create KfeCo11X64.sys binPath=C:\\\\windows\\\\temp\\\\KfeCo11X64.sys type=kernel && sc.exe start KfeCo11X64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver KfeCo11X64.sys"

# KfeCo11X64.sys

Killer exposes COM interfaces that allow non-privileged users 1) to block network for any process 2) to manage any service in the OS. Killer is preinstalled to laptops equipped with Intel Killer NICs (e.g. Dell). Since Intel patched the vulnerability quietly, it's not clear which version is safe. Also, it is unclear which OEMs are affected. Dell is definitely in the list, but it is likely that other vendors with Killer NICs on board, such as Acer and MSI, are affected too. Some users think that Killer suite is required for the NIC to work properly, so they install it even after a fresh Windows install. This version is confirmed vulnerable based on the script usage from zwclose.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068