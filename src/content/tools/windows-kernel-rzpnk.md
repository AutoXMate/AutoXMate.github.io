---
id: windows-kernel-rzpnk
namespace: windows:kernel:rzpnk
name: rzpnk.sys
description: A vulnerability exists in the latest version of Razer Synapse (v2.20.15.1104
  as of the day of disclosure) which can be leveraged locally by a malicious application
  to elevate its privileges to those of NT_AUTHORITY\SYSTEM. The vulnerability lies
  in a specific IOCTL handler in the rzpnk.sys driver that passes a PID specified
  by the user to ZwOpenProcess. CVE-2017-9769.
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
  template: sc.exe create rzpnk.sys binPath=C:\windows\temp\rzpnk.sys type=kernel
    && sc.exe start rzpnk.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load rzpnk.sys kernel driver
  commands:
  - sc.exe create rzpnk.sys binPath=C:\windows\temp\rzpnk.sys type=kernel && sc.exe
    start rzpnk.sys
detections:
- type: yara
  url: https://github.com/magicsword-io/LOLDrivers/blob/main/detections/yara/93d873cdf23d5edc622b74f9544cac7fe247d7a68e1e2a7bf2879fad97a3ae63.yara
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
  url: https://github.com/nomi-sec/PoC-in-GitHub/blob/2a85c15ed806287861a7adec6545c85aec618e3b/2017/CVE-2017-9769.json#L13
- label: Reference
  url: https://www.rapid7.com/db/modules/exploit/windows/local/razer_zwopenprocess/
features:
- local
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create rzpnk.sys binPath=C:\\\\windows\\\\temp\\\\rzpnk.sys type=kernel && sc.exe start rzpnk.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver rzpnk.sys"

# rzpnk.sys

A vulnerability exists in the latest version of Razer Synapse (v2.20.15.1104 as of the day of disclosure) which can be leveraged locally by a malicious application to elevate its privileges to those of NT_AUTHORITY\SYSTEM. The vulnerability lies in a specific IOCTL handler in the rzpnk.sys driver that passes a PID specified by the user to ZwOpenProcess. CVE-2017-9769.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
