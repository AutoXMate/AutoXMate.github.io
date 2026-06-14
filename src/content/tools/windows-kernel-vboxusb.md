---
id: windows-kernel-vboxusb
namespace: windows:kernel:vboxusb
name: VBoxUSB.Sys
description: Elevate privileges
author: Nasreddine Bencherchali
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
  template: sc.exe create VBoxUSB.sys binPath=C:\windows\temp\VBoxUSB.Sys type=kernel
    && sc.exe start VBoxUSB.Sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load VBoxUSB.Sys kernel driver
  commands:
  - sc.exe create VBoxUSB.sys binPath=C:\windows\temp\VBoxUSB.Sys type=kernel && sc.exe
    start VBoxUSB.Sys
features:
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create VBoxUSB.sys binPath=C:\\\\windows\\\\temp\\\\VBoxUSB.Sys type=kernel && sc.exe start VBoxUSB.Sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver VBoxUSB.Sys"

# VBoxUSB.Sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
