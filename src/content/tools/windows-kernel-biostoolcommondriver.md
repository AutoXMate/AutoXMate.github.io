---
id: windows-kernel-biostoolcommondriver
namespace: windows:kernel:biostoolcommondriver
name: BiosToolCommonDriver.sys
description: BiosToolCommonDriver.sys is an AMD RPMC (Replay Protected Monotonic Counter)
  field fusing utility driver that exposes 18 IOCTLs including arbitrary physical
  memory read/write via MmMapIoSpace, unrestricted port I/O, PCI configuration space
  read/write, MSR read/write (wrmsr/rdmsr), SPI flash read, CPUID execution, virtual-to-physical
  address translation via MmGetPhysicalAddress, and contiguous memory allocation.
  WHQL Microsoft-signed and also AMD Sectigo dual-signed. Ships inside Razer Blade
  1...
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
  template: sc.exe create BiosToolCommonDriver binPath=C:\windows\temp\BiosToolCommonDriver.sys
    type=kernel && sc.exe start BiosToolCommonDriver
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BiosToolCommonDriver.sys kernel driver
  commands:
  - sc.exe create BiosToolCommonDriver binPath=C:\windows\temp\BiosToolCommonDriver.sys
    type=kernel && sc.exe start BiosToolCommonDriver
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/321
features:
- file-system
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BiosToolCommonDriver binPath=C:\\\\windows\\\\temp\\\\BiosToolCommonDriver.sys type=kernel && sc.exe start BiosToolCommonDriver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BiosToolCommonDriver.sys"

# BiosToolCommonDriver.sys

BiosToolCommonDriver.sys is an AMD RPMC (Replay Protected Monotonic Counter) field fusing utility driver that exposes 18 IOCTLs including arbitrary physical memory read/write via MmMapIoSpace, unrestricted port I/O, PCI configuration space read/write, MSR read/write (wrmsr/rdmsr), SPI flash read, CPUID execution, virtual-to-physical address translation via MmGetPhysicalAddress, and contiguous memory allocation. WHQL Microsoft-signed and also AMD Sectigo dual-signed. Ships inside Razer Blade 16 BIOS update packages and ASUS firmware config bundles. PDB path confirms AMD internal build origin.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
