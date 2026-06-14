---
id: windows-kernel-msio32
namespace: windows:kernel:msio32
name: MsIo32.sys
description: The MsIo64.sys and MsIo32.sys drivers in Patriot Viper RGB before 1.1
  allow local users (including low integrity processes) to read and write to arbitrary
  memory locations, and consequently gain NT AUTHORITY\SYSTEM privileges, by mapping
  \Device\PhysicalMemory into the calling process via ZwOpenSection and ZwMapViewOfSection.
author: Michael Haag
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
  template: sc.exe create MsIo32.sys binPath=C:\windows\temp\MsIo32.sys type=kernel
    && sc.exe start MsIo32.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load MsIo32.sys kernel driver
  commands:
  - sc.exe create MsIo32.sys binPath=C:\windows\temp\MsIo32.sys type=kernel && sc.exe
    start MsIo32.sys
references:
- label: Reference
  url: https://www.activecyber.us/activelabs/viper-rgb-driver-local-privilege-escalation-cve-2019-18845
- label: Reference
  url: http://blog.rewolf.pl/blog/?p=1630
- label: Reference
  url: https://github.com/elastic/protections-artifacts/search?q=VulnDriver
features:
- file-system
- local
- network-intensive
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create MsIo32.sys binPath=C:\\\\windows\\\\temp\\\\MsIo32.sys type=kernel && sc.exe start MsIo32.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver MsIo32.sys"

# MsIo32.sys

The MsIo64.sys and MsIo32.sys drivers in Patriot Viper RGB before 1.1 allow local users (including low integrity processes) to read and write to arbitrary memory locations, and consequently gain NT AUTHORITY\SYSTEM privileges, by mapping \Device\PhysicalMemory into the calling process via ZwOpenSection and ZwMapViewOfSection.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
