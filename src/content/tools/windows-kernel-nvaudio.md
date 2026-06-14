---
id: windows-kernel-nvaudio
namespace: windows:kernel:nvaudio
name: nvaudio.sys
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
  template: sc.exe create nvaudiosys binPath= C:\windows\temp\nvaudiosys.sys type=kernel
    && sc.exe start nvaudiosys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load nvaudio.sys kernel driver
  commands:
  - sc.exe create nvaudiosys binPath= C:\windows\temp\nvaudiosys.sys type=kernel &&
    sc.exe start nvaudiosys
references:
- label: Reference
  url: https://blogs.vmware.com/security/2023/10/hunting-vulnerable-kernel-drivers.html
features:
- file-system
- local
- pipes-stdin
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create nvaudiosys binPath= C:\\\\windows\\\\temp\\\\nvaudiosys.sys type=kernel && sc.exe start nvaudiosys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver nvaudio.sys"

# nvaudio.sys

The Carbon Black Threat Analysis Unit (TAU) discovered 34 unique vulnerable drivers (237 file hashes) accepting firmware access. Six allow kernel memory access. All give full control of the devices to non-admin users. By exploiting the vulnerable drivers, an attacker without the system privilege may erase/alter firmware, and/or elevate privileges. As of the time of writing in October 2023, the filenames of the vulnerable drivers have not been made public until now.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
