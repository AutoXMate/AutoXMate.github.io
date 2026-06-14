---
id: windows-kernel-appshopdrv103
namespace: windows:kernel:appshopdrv103
name: "AppShopDrv103.sys"
description: "AppShopDrv103.sys is a hardware utility driver from ASRock distributed with APP Shop and Auto Driver Installer. The driver exposes 30+ IOCTLs through a BCrypt AES-encrypted command wrapper (IOCTL 0x22EC00) with a hardcoded key, providing arbitrary physical memory read and write via MmMapIoSpace (IOCTLs 0x22E808/0x22E80C), unrestricted I/O port read and write in byte, word, and dword widths (IOCTLs 0x22E810-0x22E824), full PCI configuration space read and write via port 0xCF8/0xCFC (IOCTLs 0x2..."
author: "Michael Haag"
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
  template: "sc.exe create AppShopDrv103 binPath=C:\\windows\\temp\\AppShopDrv103.sys type=kernel && sc.exe start AppShopDrv103"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load AppShopDrv103.sys kernel driver"
    commands:
      - "sc.exe create AppShopDrv103 binPath=C:\\windows\\temp\\AppShopDrv103.sys type=kernel && sc.exe start AppShopDrv103"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/222"
  - label: "Reference"
    url: "https://github.com/hfiref0x/KDU"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create AppShopDrv103 binPath=C:\\\\windows\\\\temp\\\\AppShopDrv103.sys type=kernel && sc.exe start AppShopDrv103"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver AppShopDrv103.sys"

# AppShopDrv103.sys

AppShopDrv103.sys is a hardware utility driver from ASRock distributed with APP Shop and Auto Driver Installer. The driver exposes 30+ IOCTLs through a BCrypt AES-encrypted command wrapper (IOCTL 0x22EC00) with a hardcoded key, providing arbitrary physical memory read and write via MmMapIoSpace (IOCTLs 0x22E808/0x22E80C), unrestricted I/O port read and write in byte, word, and dword widths (IOCTLs 0x22E810-0x22E824), full PCI configuration space read and write via port 0xCF8/0xCFC (IOCTLs 0x22E830-0x22E844), MSR read and write via rdmsr/wrmsr (IOCTLs 0x22E848/0x22E84C), control register reads for CR0/CR2/CR3/CR4/CR8 (IOCTL 0x22E86C), RDTSC and RDPMC performance counter access, CPUID execution, and contiguous memory allocation. Same vulnerability class as other ASRock drivers (AsrDrv.sys) already tracked in LOLDrivers. Used by KDU (Kernel Driver Utility) as a provider.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068