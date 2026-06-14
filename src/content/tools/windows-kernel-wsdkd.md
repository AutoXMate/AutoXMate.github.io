---
id: windows-kernel-wsdkd
namespace: windows:kernel:wsdkd
name: wsdkd.sys
description: A vulnerability was found in Watchdog Anti-Virus 1.4.214.0. It has been
  rated as critical. Affected by this issue is the function 0x80002008 in the library
  wsdk-driver.sys of the component IoControlCode Handler. The manipulation leads to
  improper access controls. Attacking locally is a requirement. The exploit has been
  disclosed to the public and may be used. VDB-223298 is the identifier assigned to
  this vulnerability.
author: Chris Beckett, Jon Petersen
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
  template: sc.exe create wsdkd.sys binPath=C:\windows\temp\wsdkd.sys type=kernel
    && sc.exe start wsdkd.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load wsdkd.sys kernel driver
  commands:
  - sc.exe create wsdkd.sys binPath=C:\windows\temp\wsdkd.sys type=kernel && sc.exe
    start wsdkd.sys
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
  url: https://github.com/zeze-zeze/WindowsKernelVuln/tree/master/CVE-2023-1453
- label: Reference
  url: https://nvd.nist.gov/vuln/detail/CVE-2023-1453
- label: Reference
  url: https://avd.aquasec.com/nvd/2023/cve-2023-1453/
features:
- local
- pipes-stdin
- requires-root
- streaming
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create wsdkd.sys binPath=C:\\\\windows\\\\temp\\\\wsdkd.sys type=kernel && sc.exe start wsdkd.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver wsdkd.sys"

# wsdkd.sys

A vulnerability was found in Watchdog Anti-Virus 1.4.214.0. It has been rated as critical. Affected by this issue is the function 0x80002008 in the library wsdk-driver.sys of the component IoControlCode Handler. The manipulation leads to improper access controls. Attacking locally is a requirement. The exploit has been disclosed to the public and may be used. VDB-223298 is the identifier assigned to this vulnerability.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
