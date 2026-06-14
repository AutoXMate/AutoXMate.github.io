---
id: windows-kernel-astra64
namespace: windows:kernel:astra64
name: Astra64.sys
description: ASTRA64.sys is the kernel driver for the ASTRA32 system information tool
  by Sysinfo Lab (EnTech Taiwan). The driver exposes 31 IOCTLs with zero validation
  on all parameters including arbitrary physical memory read/write via ZwOpenSection
  and ZwMapViewOfSection on Device\PhysicalMemory with PAGE_READWRITE, arbitrary port
  I/O via HalTranslateBusAddress, arbitrary MSR read via rdmsr (enables KASLR bypass
  via IA32_LSTAR), PCI configuration space read via HalGetBusDataByOffset, and MMIO
  physical m...
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
  template: sc.exe create Astra64 binPath=C:\windows\temp\Astra64.sys type=kernel
    && sc.exe start Astra64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load Astra64.sys kernel driver
  commands:
  - sc.exe create Astra64 binPath=C:\windows\temp\Astra64.sys type=kernel && sc.exe
    start Astra64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/294
- label: Reference
  url: https://eclypsium.com/research/screwed-drivers-signed-sealed-delivered/
features:
- compression
- file-system
- requires-root
- stealth
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create Astra64 binPath=C:\\\\windows\\\\temp\\\\Astra64.sys type=kernel && sc.exe start Astra64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver Astra64.sys"

# Astra64.sys

ASTRA64.sys is the kernel driver for the ASTRA32 system information tool by Sysinfo Lab (EnTech Taiwan). The driver exposes 31 IOCTLs with zero validation on all parameters including arbitrary physical memory read/write via ZwOpenSection and ZwMapViewOfSection on Device\PhysicalMemory with PAGE_READWRITE, arbitrary port I/O via HalTranslateBusAddress, arbitrary MSR read via rdmsr (enables KASLR bypass via IA32_LSTAR), PCI configuration space read via HalGetBusDataByOffset, and MMIO physical memory mapping via MmMapIoSpace. No authentication gate, no DACL restrictions (plain IoCreateDevice). Loads on any x64 Windows system. EnTech Taiwan also produces TVicPort and softEngine drivers which share similar low-level hardware access patterns. Listed in Eclypsium Screwed-Drivers research.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
