---
id: windows-kernel-blacklotus-driver
namespace: windows:kernel:blacklotus-driver
name: "blacklotus_driver.sys"
description: "The first in-the-wild UEFI bootkit bypassing UEFI Secure Boot on fully updated UEFI systems is now a reality. Once the persistence is configured, the BlackLotus bootkit is executed on every system start. The bootkits goal is to deploy a kernel driver and a final user-mode component."
author: "Michael Haag"
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
  template: "sc.exe create blacklotus_driver.sys binPath=C:\\windows\\temp\\blacklotus_driver.sys type=kernel && sc.exe start blacklotus_driver.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load blacklotus_driver.sys kernel driver"
    commands:
      - "sc.exe create blacklotus_driver.sys binPath=C:\\windows\\temp\\blacklotus_driver.sys type=kernel && sc.exe start blacklotus_driver.sys"
references:
  - label: "Reference"
    url: "https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create blacklotus_driver.sys binPath=C:\\\\windows\\\\temp\\\\blacklotus_driver.sys type=kernel && sc.exe start blacklotus_driver.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver blacklotus_driver.sys"

# blacklotus_driver.sys

The first in-the-wild UEFI bootkit bypassing UEFI Secure Boot on fully updated UEFI systems is now a reality. Once the persistence is configured, the BlackLotus bootkit is executed on every system start. The bootkits goal is to deploy a kernel driver and a final user-mode component.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068