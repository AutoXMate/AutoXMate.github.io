---
id: windows-kernel-bsitf
namespace: windows:kernel:bsitf
name: bsitf.sys
description: bsitf.sys is the ASUS BIOS Flash Driver distributed with ASUS WinFlash
  BIOS update utility. The driver persists on disk after WinFlash completes and exposes
  physical memory read via MmMapIoSpace (IOCTL 0x222804), physically contiguous kernel
  memory allocation mapped to usermode via MDL (IOCTL 0x222808), arbitrary I/O port
  write (IOCTL 0x222810) and read (IOCTL 0x222818), PCI config space read with BAR
  mapping to usermode (IOCTL 0x222814), and BIOS flash write via MmMapIoSpace (IOCTL
  0x22281c)...
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
  template: sc.exe create bsitf binPath=C:\windows\temp\bsitf.sys type=kernel && sc.exe
    start bsitf
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load bsitf.sys kernel driver
  commands:
  - sc.exe create bsitf binPath=C:\windows\temp\bsitf.sys type=kernel && sc.exe start
    bsitf
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/pull/332
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- local
- network-intensive
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create bsitf binPath=C:\\\\windows\\\\temp\\\\bsitf.sys type=kernel && sc.exe start bsitf"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver bsitf.sys"

# bsitf.sys

bsitf.sys is the ASUS BIOS Flash Driver distributed with ASUS WinFlash BIOS update utility. The driver persists on disk after WinFlash completes and exposes physical memory read via MmMapIoSpace (IOCTL 0x222804), physically contiguous kernel memory allocation mapped to usermode via MDL (IOCTL 0x222808), arbitrary I/O port write (IOCTL 0x222810) and read (IOCTL 0x222818), PCI config space read with BAR mapping to usermode (IOCTL 0x222814), and BIOS flash write via MmMapIoSpace (IOCTL 0x22281c). WHQL attestation signed via Microsoft Windows Third Party Component CA 2014. Device SDDL grants full access to Administrators group.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
