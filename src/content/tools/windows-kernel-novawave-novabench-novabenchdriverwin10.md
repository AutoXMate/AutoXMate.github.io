---
id: windows-kernel-novawave-novabench-novabenchdriverwin10
namespace: windows:kernel:novawave-novabench-novabenchdriverwin10
name: Novawave_Novabench_NovabenchDriverWin10.sys
description: Novawave_Novabench_NovabenchDriverWin10.sys is a vulnerable kernel driver
  from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes
  dangerous kernel primitives to usermode.
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
  template: sc.exe create Novawave_Novabench_NovabenchDriverWin10 binPath=C:\windows\temp\Novawave_Novabench_NovabenchDriverWin10.sys
    type=kernel && sc.exe start Novawave_Novabench_NovabenchDriverWin10
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Novawave_Novabench_NovabenchDriverWin10.sys kernel driver
  commands:
  - sc.exe create Novawave_Novabench_NovabenchDriverWin10 binPath=C:\windows\temp\Novawave_Novabench_NovabenchDriverWin10.sys
    type=kernel && sc.exe start Novawave_Novabench_NovabenchDriverWin10
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Novawave_Novabench_NovabenchDriverWin10 binPath=C:\\\\windows\\\\temp\\\\Novawave_Novabench_NovabenchDriverWin10.sys type=kernel && sc.exe start Novawave_Novabench_NovabenchDriverWin10"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Novawave_Novabench_NovabenchDriverWin10.sys"

# Novawave_Novabench_NovabenchDriverWin10.sys

Novawave_Novabench_NovabenchDriverWin10.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
