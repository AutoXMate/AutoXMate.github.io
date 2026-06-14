---
id: windows-kernel-fh-ethercat-dio
namespace: windows:kernel:fh-ethercat-dio
name: FH-EtherCAT_DIO.sys
description: The Carbon Black Threat Analysis Unit (TAU) discovered 34 unique vulnerable
  drivers (237 file hashes) accepting firmware access. Six allow kernel memory access.
  All give full control of the devices to non-admin users. By exploiting the vulnerable
  drivers, an attacker without the system privilege may erase/alter firmware, and/or
  elevate privileges. As of the time of writing in October 2023, the filenames of
  the vulnerable drivers have not been made public until now.
author: Takahiro Haruyama
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
  template: sc.exe create FH-EtherCAT_DIOsys binPath= C:\windows\temp\FH-EtherCAT_DIOsys.sys
    type=kernel && sc.exe start FH-EtherCAT_DIOsys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load FH-EtherCAT_DIO.sys kernel driver
  commands:
  - sc.exe create FH-EtherCAT_DIOsys binPath= C:\windows\temp\FH-EtherCAT_DIOsys.sys
    type=kernel && sc.exe start FH-EtherCAT_DIOsys
references:
- label: Reference
  url: https://blogs.vmware.com/security/2023/10/hunting-vulnerable-kernel-drivers.html
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create FH-EtherCAT_DIOsys binPath= C:\\\\windows\\\\temp\\\\FH-EtherCAT_DIOsys.sys type=kernel && sc.exe start FH-EtherCAT_DIOsys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver FH-EtherCAT_DIO.sys"

# FH-EtherCAT_DIO.sys

The Carbon Black Threat Analysis Unit (TAU) discovered 34 unique vulnerable drivers (237 file hashes) accepting firmware access. Six allow kernel memory access. All give full control of the devices to non-admin users. By exploiting the vulnerable drivers, an attacker without the system privilege may erase/alter firmware, and/or elevate privileges. As of the time of writing in October 2023, the filenames of the vulnerable drivers have not been made public until now.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
