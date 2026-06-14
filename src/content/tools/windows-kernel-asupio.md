---
id: windows-kernel-asupio
namespace: windows:kernel:asupio
name: "AsUpIO.sys"
description: "Elevate privileges"
author: "Michael Haag, Nasreddine Bencherchali"
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
  template: "sc.exe create AsUpIO.sys binPath=C:\\windows\\temp\\AsUpIO.sys type=kernel && sc.exe start AsUpIO.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load AsUpIO.sys kernel driver"
    commands:
      - "sc.exe create AsUpIO.sys binPath=C:\\windows\\temp\\AsUpIO.sys type=kernel && sc.exe start AsUpIO.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
  - label: "Reference"
    url: "https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.m"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AsUpIO.sys binPath=C:\\\\windows\\\\temp\\\\AsUpIO.sys type=kernel && sc.exe start AsUpIO.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AsUpIO.sys"

# AsUpIO.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068