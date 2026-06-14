---
id: windows-kernel-filwfp
namespace: windows:kernel:filwfp
name: filwfp.sys
description: 'Twister Antivirus, fildds.sys, DoS2

  CVE-2023-1444

  From IoControlCode 0x8011206B, a normal user can cause DoS due to writing into null
  address.'
author: VirarK
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
  template: sc.exe create filwfp.sys binPath=C:\windows\temp\filwfp.sys type=kernel
    && sc.exe start filwfp.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load filwfp.sys kernel driver
  commands:
  - sc.exe create filwfp.sys binPath=C:\windows\temp\filwfp.sys type=kernel && sc.exe
    start filwfp.sys
references:
- label: Reference
  url: https://github.com/zeze-zeze/WindowsKernelVuln/tree/master/CVE-2023-1444
features:
- file-system
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create filwfp.sys binPath=C:\\\\windows\\\\temp\\\\filwfp.sys type=kernel && sc.exe start filwfp.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver filwfp.sys"

# filwfp.sys

Twister Antivirus, fildds.sys, DoS2

    CVE-2023-1444

    From IoControlCode 0x8011206B, a normal user can cause DoS due to writing into
    null address.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
