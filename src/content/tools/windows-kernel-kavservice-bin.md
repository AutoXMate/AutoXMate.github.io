---
id: windows-kernel-kavservice-bin
namespace: windows:kernel:kavservice-bin
name: kavservice.bin
description: EDR Kill
author: Antonio Parata, Andrea Monzani
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- defense-evasion
risk_level: critical
trust_level: verified
execution:
  template: sc.exe create kavservice.sys binPath=C:\windows\temp\kavservice.sys type=kernel
    && sc.exe start kavservice.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load kavservice.bin kernel driver
  commands:
  - sc.exe create kavservice.sys binPath=C:\windows\temp\kavservice.sys type=kernel
    && sc.exe start kavservice.sys
references:
- label: Reference
  url: https://www.52pojie.cn/thread-1823439-1-1.html
features:
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create kavservice.sys binPath=C:\\\\windows\\\\temp\\\\kavservice.sys type=kernel && sc.exe start kavservice.sys"

# kavservice.bin

**Use Case:** EDR Kill

**Required Privileges:** Admin privileges

**MITRE ATT&CK:** T1562
