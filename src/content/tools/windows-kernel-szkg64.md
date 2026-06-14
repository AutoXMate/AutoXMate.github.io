---
id: windows-kernel-szkg64
namespace: windows:kernel:szkg64
name: szkg64.sys
description: The StopZilla driver is a forgotten but still exploitable vulnerable
  driver that allows arbitrary kernel memory writes via unvalidated IOCTLs (0x80002063
  and 0x8000206F). Attackers can leverage it to escalate privileges, disable LSASS
  PPL protection, and even modify PreviousMode in _KTHREAD to execute user-mode code
  as kernel-mode, effectively bypassing security checks. Despite its risks, it remains
  unblocked by Microsoft’s Driver Block List and many AV/EDR solutions. This driver
  highlights t...
author: decoder
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
  template: sc.exe create szkg64.sys binPath=C:\windows\temp\szkg64.sys type=kernel
    && sc.exe start szkg64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load szkg64.sys kernel driver
  commands:
  - sc.exe create szkg64.sys binPath=C:\windows\temp\szkg64.sys type=kernel && sc.exe
    start szkg64.sys
references:
- label: Reference
  url: https://www.greyhathacker.net/?p=1025
- label: Reference
  url: https://decoder.cloud/2025/01/09/the-almost-forgotten-vulnerable-driver/
features:
- file-system
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
- stealth
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create szkg64.sys binPath=C:\\\\windows\\\\temp\\\\szkg64.sys type=kernel && sc.exe start szkg64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver szkg64.sys"

# szkg64.sys

The StopZilla driver is a forgotten but still exploitable vulnerable driver that allows arbitrary kernel memory writes via unvalidated IOCTLs (0x80002063 and 0x8000206F). Attackers can leverage it to escalate privileges, disable LSASS PPL protection, and even modify PreviousMode in _KTHREAD to execute user-mode code as kernel-mode, effectively bypassing security checks. Despite its risks, it remains unblocked by Microsoft’s Driver Block List and many AV/EDR solutions. This driver highlights the persistent threat of forgotten vulnerable drivers still exploitable in modern Windows environments.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
