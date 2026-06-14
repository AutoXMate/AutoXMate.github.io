---
id: windows-kernel-winio64
namespace: windows:kernel:winio64
name: WinIo64.sys
description: WinIo64.sys is a hardware access driver based on the WinIo library that
  provides direct physical memory access and I/O port operations from usermode. The
  driver maps the \Device\PhysicalMemory section object to user space via ZwOpenSection
  and ZwMapViewOfSection (IOCTL 0x80102040), with corresponding unmap (IOCTL 0x80102044),
  and provides arbitrary I/O port read (IOCTL 0x80102050) and write (IOCTL 0x80102054)
  in byte, word, and dword widths. Physical address translation via HalTranslateBusAdd...
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
  template: sc.exe create WinIo64 binPath=C:\windows\temp\WinIo64.sys type=kernel
    && sc.exe start WinIo64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load WinIo64.sys kernel driver
  commands:
  - sc.exe create WinIo64 binPath=C:\windows\temp\WinIo64.sys type=kernel && sc.exe
    start WinIo64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/222
- label: Reference
  url: https://github.com/hfiref0x/KDU
features:
- file-system
- network-intensive
- pipes-stdin
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WinIo64 binPath=C:\\\\windows\\\\temp\\\\WinIo64.sys type=kernel && sc.exe start WinIo64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WinIo64.sys"

# WinIo64.sys

WinIo64.sys is a hardware access driver based on the WinIo library that provides direct physical memory access and I/O port operations from usermode. The driver maps the \Device\PhysicalMemory section object to user space via ZwOpenSection and ZwMapViewOfSection (IOCTL 0x80102040), with corresponding unmap (IOCTL 0x80102044), and provides arbitrary I/O port read (IOCTL 0x80102050) and write (IOCTL 0x80102054) in byte, word, and dword widths. Physical address translation via HalTranslateBusAddress is also available. WHQL attestation signed via Microsoft Windows Third Party Component CA 2014. Distributed by multiple OEM utilities and heavily abused in the wild with 61 malicious execution parents on VT including malware droppers and BYOVD tools. Used by KDU (Kernel Driver Utility) as a provider.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
