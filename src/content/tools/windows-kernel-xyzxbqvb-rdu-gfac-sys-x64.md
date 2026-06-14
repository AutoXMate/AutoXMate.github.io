---
id: windows-kernel-xyzxbqvb-rdu-gfac-sys-x64
namespace: windows:kernel:xyzxbqvb-rdu-gfac-sys-x64
name: "_xyzxbqvb.rdu_GFAC_Sys_x64.sys"
description: "_xyzxbqvb.rdu_GFAC_Sys_x64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create _xyzxbqvb.rdu_GFAC_Sys_x64 binPath=C:\\windows\\temp\\_xyzxbqvb.rdu_GFAC_Sys_x64.sys type=kernel && sc.exe start _xyzxbqvb.rdu_GFAC_Sys_x64"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load _xyzxbqvb.rdu_GFAC_Sys_x64.sys kernel driver"
    commands:
      - "sc.exe create _xyzxbqvb.rdu_GFAC_Sys_x64 binPath=C:\\windows\\temp\\_xyzxbqvb.rdu_GFAC_Sys_x64.sys type=kernel && sc.exe start _xyzxbqvb.rdu_GFAC_Sys_x64"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create _xyzxbqvb.rdu_GFAC_Sys_x64 binPath=C:\\\\windows\\\\temp\\\\_xyzxbqvb.rdu_GFAC_Sys_x64.sys type=kernel && sc.exe start _xyzxbqvb.rdu_GFAC_Sys_x64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver _xyzxbqvb.rdu_GFAC_Sys_x64.sys"

# _xyzxbqvb.rdu_GFAC_Sys_x64.sys

_xyzxbqvb.rdu_GFAC_Sys_x64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068