---
id: windows-kernel-rtsuer
namespace: windows:kernel:rtsuer
name: RtsUer.sys
description: The Realtek SD card reader driver, RtsUer.sys, versions below or equal
  to 10.0.22000.31273 contain multiple vulnerabilities that pose significant security
  risks. These flaws allow non-privileged users to write to kernel memory and access
  the DMA controller from unprivileged accounts, potentially enabling privilege escalation
  and system compromise. The most severe issues include the ability to write to kernel
  memory and access the DMA controller, which could lead to unauthorized system modific...
author: Michael M.
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
  template: sc.exe create RtsUer.sys binPath=C:\windows\temp\RtsUer.sys type=kernel
    && sc.exe start RtsUer.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load RtsUer.sys kernel driver
  commands:
  - sc.exe create RtsUer.sys binPath=C:\windows\temp\RtsUer.sys type=kernel && sc.exe
    start RtsUer.sys
references:
- label: Reference
  url: https://www.linkedin.com/pulse/vulnerabilities-realtek-sd-card-reader-driver-part-1-myngerbayev-czqmf,
    https://github.com/zwclose/realteksd
features:
- file-system
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create RtsUer.sys binPath=C:\\\\windows\\\\temp\\\\RtsUer.sys type=kernel && sc.exe start RtsUer.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver RtsUer.sys"

# RtsUer.sys

The Realtek SD card reader driver, RtsUer.sys, versions below or equal to 10.0.22000.31273 contain multiple vulnerabilities that pose significant security risks. These flaws allow non-privileged users to write to kernel memory and access the DMA controller from unprivileged accounts, potentially enabling privilege escalation and system compromise. The most severe issues include the ability to write to kernel memory and access the DMA controller, which could lead to unauthorized system modifications. These vulnerabilities affect various Realtek SD card reader models used by major OEM laptop manufacturers. Due to the widespread use of this driver, the impact is considerable, potentially affecting a large number of systems across different brands. Users with laptops equipped with Realtek SD card readers should ensure their drivers are updated to a version higher than 10.0.22000.31273 to mitigate these security risks.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
