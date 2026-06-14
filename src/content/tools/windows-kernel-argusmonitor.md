---
id: windows-kernel-argusmonitor
namespace: windows:kernel:argusmonitor
name: ArgusMonitor.sys
description: ArgusMonitor.sys is the kernel driver for the Argus Monitor hardware
  temperature monitoring and fan control application by Argotronic UG (Germany). The
  driver exposes 47 IOCTLs providing arbitrary physical memory read/write via MmMapIoSpace
  (32 map slots, up to 128KB) with a single-shot read primitive that bypasses the
  address restriction (busNum=0xFF), unrestricted port I/O (any port 0x0000-0xFFFF),
  PCI configuration space read/write via HalGetBusDataByOffset and HalSetBusDataByOffset,
  MSR r...
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
  template: sc.exe create ArgusMonitor binPath=C:\windows\temp\ArgusMonitor.sys type=kernel
    && sc.exe start ArgusMonitor
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ArgusMonitor.sys kernel driver
  commands:
  - sc.exe create ArgusMonitor binPath=C:\windows\temp\ArgusMonitor.sys type=kernel
    && sc.exe start ArgusMonitor
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/297
- label: Reference
  url: https://www.argusmonitor.com/
features:
- file-system
- pipes-stdout
- requires-root
- stealth
- streaming
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ArgusMonitor binPath=C:\\\\windows\\\\temp\\\\ArgusMonitor.sys type=kernel && sc.exe start ArgusMonitor"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ArgusMonitor.sys"

# ArgusMonitor.sys

ArgusMonitor.sys is the kernel driver for the Argus Monitor hardware temperature monitoring and fan control application by Argotronic UG (Germany). The driver exposes 47 IOCTLs providing arbitrary physical memory read/write via MmMapIoSpace (32 map slots, up to 128KB) with a single-shot read primitive that bypasses the address restriction (busNum=0xFF), unrestricted port I/O (any port 0x0000-0xFFFF), PCI configuration space read/write via HalGetBusDataByOffset and HalSetBusDataByOffset, MSR read/write with a whitelist that blocks IA32_LSTAR but allows IA32_MISC_ENABLE write (can disable NX/XD system-wide), and I2C/SMBus access via MMIO bit-banging. The driver uses IoCreateDevice with no DACL and IRP_MJ_CREATE returns STATUS_SUCCESS immediately with no caller validation. A handshake IOCTL accepts a user-chosen 0x200-byte XOR keypad (sending all zeros effectively disables the XOR layer). WHQL attestation signed with an active Microsoft certificate. KASLR bypass confirmed via physical memory PE header scan. Loads on any x64 Windows without ArgusMonitor software.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
