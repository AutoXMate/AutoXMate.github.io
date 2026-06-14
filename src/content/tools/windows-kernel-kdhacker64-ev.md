---
id: windows-kernel-kdhacker64-ev
namespace: windows:kernel:kdhacker64-ev
name: "kdhacker64_ev.sys"
description: "kdhacker64_ev.sys is a kernel driver from Beijing Kingsoft Security software bundled with Kingsoft AntiVirus and Liebao Browser. The driver exposes a kernel heap buffer overflow via IOCTL 0x120140 with approximately 512 bytes of overflow into adjacent kernel pool allocations. The root cause is a size validation mismatch -- input is validated at 0x488 bytes per element but only 0x248 bytes are allocated per element. RtlInitUnicodeString is called on user-controlled buffers without null termina..."
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
  template: "sc.exe create KDHacker binPath=C:\\windows\\temp\\kdhacker64_ev.sys type=kernel && sc.exe start KDHacker"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load kdhacker64_ev.sys kernel driver"
    commands:
      - "sc.exe create KDHacker binPath=C:\\windows\\temp\\kdhacker64_ev.sys type=kernel && sc.exe start KDHacker"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/309"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create KDHacker binPath=C:\\\\windows\\\\temp\\\\kdhacker64_ev.sys type=kernel && sc.exe start KDHacker"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver kdhacker64_ev.sys"

# kdhacker64_ev.sys

kdhacker64_ev.sys is a kernel driver from Beijing Kingsoft Security software bundled with Kingsoft AntiVirus and Liebao Browser. The driver exposes a kernel heap buffer overflow via IOCTL 0x120140 with approximately 512 bytes of overflow into adjacent kernel pool allocations. The root cause is a size validation mismatch -- input is validated at 0x488 bytes per element but only 0x248 bytes are allocated per element. RtlInitUnicodeString is called on user-controlled buffers without null terminator bounds checking, producing oversized ANSI strings that overflow 64-byte destination buffers. No authentication is required to access the device. The driver also includes TDI hooks for TCP/UDP/RawIP interception, process creation notification callbacks, filesystem filter attachments to NTFS/FAT/CDFS, camera device monitoring, and HTTP header parsing. Other Kingsoft drivers (ksapi.sys, mydrivers.sys) are already tracked in LOLDrivers.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068