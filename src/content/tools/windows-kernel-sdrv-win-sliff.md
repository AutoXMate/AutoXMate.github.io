---
id: windows-kernel-sdrv-win-sliff
namespace: windows:kernel:sdrv-win-sliff
name: "sdrv_win_sliff.sys"
description: "sdrv_win_sliff.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
author: "Michael Haag"
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
  template: "sc.exe create sdrv_win_sliff binPath=C:\\windows\\temp\\sdrv_win_sliff.sys type=kernel && sc.exe start sdrv_win_sliff"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load sdrv_win_sliff.sys kernel driver"
    commands:
      - "sc.exe create sdrv_win_sliff binPath=C:\\windows\\temp\\sdrv_win_sliff.sys type=kernel && sc.exe start sdrv_win_sliff"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create sdrv_win_sliff binPath=C:\\\\windows\\\\temp\\\\sdrv_win_sliff.sys type=kernel && sc.exe start sdrv_win_sliff"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver sdrv_win_sliff.sys"

# sdrv_win_sliff.sys

sdrv_win_sliff.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068