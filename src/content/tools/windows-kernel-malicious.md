---
id: windows-kernel-malicious
namespace: windows:kernel:malicious
name: "malicious.sys"
description: "This demo is a presentation at the CYBERSEC 2023 in Taiwan. The presentation showcases the abuse of RTCore64.sys (CVE-2019-16098) from MSI and the nullification of the DSE flag to load a malicious unsigned driver. The presentation also demonstrates an attack on 360 Total Security by nulling out its ObRegisterCallbacks and notify callbacks, enabling the execution of any malicious behavior on the processes of 360 Total Security."
author: "Guus Verbeek"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: "sc.exe create malicious.sys binPath=C:\\windows\\temp\\malicious.sys type=kernel && sc.exe start malicious.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load malicious.sys kernel driver"
    commands:
      - "sc.exe create malicious.sys binPath=C:\\windows\\temp\\malicious.sys type=kernel && sc.exe start malicious.sys"
references:
  - label: "Reference"
    url: "https://github.com/zeze-zeze/CYBERSEC2023-BYOVD-Demo"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create malicious.sys binPath=C:\\\\windows\\\\temp\\\\malicious.sys type=kernel && sc.exe start malicious.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver malicious.sys"

# malicious.sys

This demo is a presentation at the CYBERSEC 2023 in Taiwan. The presentation showcases the abuse of RTCore64.sys (CVE-2019-16098) from MSI and the nullification of the DSE flag to load a malicious unsigned driver. The presentation also demonstrates an attack on 360 Total Security by nulling out its ObRegisterCallbacks and notify callbacks, enabling the execution of any malicious behavior on the processes of 360 Total Security.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068