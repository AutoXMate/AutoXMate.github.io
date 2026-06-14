---
id: windows-kernel-dtr-ec
namespace: windows:kernel:dtr-ec
name: dtr_ec.sys
description: dtr_ec.sys is a Dell kernel driver that ships as part of the Dell Feature
  Enhancement Pack (DFEP) on Dell laptops and desktops. The driver provides unrestricted
  read/write access to Embedded Controller (EC) registers across 5 ACPI address spaces
  from usermode with no validation on the register addresses or values. The Embedded
  Controller manages critical hardware functions including thermal management, battery
  charging, fan control, power states, and keyboard input. Unrestricted EC register
  a...
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: high
trust_level: community
execution:
  template: sc.exe create dtr_ec binPath=C:\windows\temp\dtr_ec.sys type=kernel &&
    sc.exe start dtr_ec
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dtr_ec.sys kernel driver
  commands:
  - sc.exe create dtr_ec binPath=C:\windows\temp\dtr_ec.sys type=kernel && sc.exe
    start dtr_ec
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/293
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dtr_ec binPath=C:\\\\windows\\\\temp\\\\dtr_ec.sys type=kernel && sc.exe start dtr_ec"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dtr_ec.sys"

# dtr_ec.sys

dtr_ec.sys is a Dell kernel driver that ships as part of the Dell Feature Enhancement Pack (DFEP) on Dell laptops and desktops. The driver provides unrestricted read/write access to Embedded Controller (EC) registers across 5 ACPI address spaces from usermode with no validation on the register addresses or values. The Embedded Controller manages critical hardware functions including thermal management, battery charging, fan control, power states, and keyboard input. Unrestricted EC register access allows manipulation of thermal thresholds to cause hardware damage or forced shutdowns, modification of fan speed controls, interference with battery charging logic, and alteration of power management behavior. Dell PSIRT has confirmed the vulnerability and triaged it as P2 severity on Bugcrowd.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
