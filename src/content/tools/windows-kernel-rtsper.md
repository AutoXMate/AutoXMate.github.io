---
id: windows-kernel-rtsper
namespace: windows:kernel:rtsper
name: "RtsPer.sys"
description: "The Realtek SD card reader driver, RtsPer.sys, has been found to contain multiple critical vulnerabilities (CVE-2022-25476, CVE-2022-25477, CVE-2022-25478, CVE-2022-25479, CVE-2022-25480, CVE-2024-40431, CVE-2024-40432) that allow non-privileged users to leak kernel memory, write to arbitrary kernel memory, and access physical memory via DMA. These flaws affect various SD card reader models (including RTS5227, RTS5228, RTS522A, RTS5249, RTS524A, RTS5250, RTS525A, RTS5287, RTS5260, RTS5261, RT..."
author: "Michael M."
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
  template: "sc.exe create RtsPer.sys binPath=C:\\windows\\temp\\RtsPer.sys type=kernel && sc.exe start RtsPer.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load RtsPer.sys kernel driver"
    commands:
      - "sc.exe create RtsPer.sys binPath=C:\\windows\\temp\\RtsPer.sys type=kernel && sc.exe start RtsPer.sys"
references:
  - label: "Reference"
    url: "https://www.linkedin.com/pulse/vulnerabilities-realtek-sd-card-reader-driver-part-1-myngerbayev-czqmf, https://github.com/zwclose/realteksd"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create RtsPer.sys binPath=C:\\\\windows\\\\temp\\\\RtsPer.sys type=kernel && sc.exe start RtsPer.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver RtsPer.sys"

# RtsPer.sys

The Realtek SD card reader driver, RtsPer.sys, has been found to contain multiple critical vulnerabilities (CVE-2022-25476, CVE-2022-25477, CVE-2022-25478, CVE-2022-25479, CVE-2022-25480, CVE-2024-40431, CVE-2024-40432) that allow non-privileged users to leak kernel memory, write to arbitrary kernel memory, and access physical memory via DMA. These flaws affect various SD card reader models (including RTS5227, RTS5228, RTS522A, RTS5249, RTS524A, RTS5250, RTS525A, RTS5287, RTS5260, RTS5261, RTS5264) used by major OEMs such as Dell, Lenovo, HP, and MSI. The vulnerabilities enable kernel memory leaks, arbitrary kernel memory writes, PCI configuration space manipulation, and DMA controller access from user mode. Due to the driver's widespread use, the impact is significant, potentially allowing privilege escalation and system compromise. Realtek has addressed these issues in driver version 10.0.26100.21374 or higher, released in July or August. 

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068