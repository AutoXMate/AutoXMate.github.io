---
id: windows-kernel-mhyprot2
namespace: windows:kernel:mhyprot2
name: Mhyprot2.sys
description: Elevate privileges
author: Nasreddine Bencherchali, Michael Haag
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
  template: sc.exe create mhyprot.sys binPath=C:\windows\temp\mhyprot.sys type=kernel
    && sc.exe start mhyprot.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Mhyprot2.sys kernel driver
  commands:
  - sc.exe create mhyprot.sys binPath=C:\windows\temp\mhyprot.sys type=kernel && sc.exe
    start mhyprot.sys
references:
- label: Reference
  url: https://github.com/namazso/physmem_drivers
- label: Reference
  url: https://github.com/jbaines-r7/dellicious
- label: Reference
  url: https://www.rapid7.com/blog/post/2021/12/13/driver-based-attacks-past-and-present/
- label: Reference
  url: https://github.com/elastic/protections-artifacts/blob/932baf346cc8a743f1963ad3d4565b42ed17bebe/yara/rules/Windows_VulnDriver_Mhyprot.yar
- label: Reference
  url: https://gist.github.com/mgraeber-rc/1bde6a2a83237f17b463d051d32e802c
- label: Reference
  url: https://github.com/kagurazakasanae/Mhyprot2DrvControl/tree/main
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create mhyprot.sys binPath=C:\\\\windows\\\\temp\\\\mhyprot.sys type=kernel && sc.exe start mhyprot.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Mhyprot2.sys"

# Mhyprot2.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
