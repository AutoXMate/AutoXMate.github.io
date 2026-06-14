---
id: windows-kernel-tvicport64
namespace: windows:kernel:tvicport64
name: TVicPort64.sys
description: Load TVicPort64.sys kernel driver. Once loaded, device \\.\TVicPortDevice0
  is accessible from any integrity level (no DACL). Send IOCTL 0x80002008 to map arbitrary
  physical memory into user-mode VA space via ZwMapViewOfSection and perform token
  stealing for LPE to SYSTEM.
author: Joao Leko Monteiro
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
  template: sc.exe create TVicPort64 binPath=C:\windows\temp\TVicPort64.sys type=kernel
    && sc.exe start TVicPort64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load TVicPort64.sys kernel driver
  commands:
  - sc.exe create TVicPort64 binPath=C:\windows\temp\TVicPort64.sys type=kernel &&
    sc.exe start TVicPort64
detections:
- type: other
  description: Detect load of TVicPort64.sys by hash or device name \\.\TVicPortDevice0
references:
- label: Reference
  url: https://www.entechtaiwan.com/dev/port/index.shtm
features:
- file-system
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TVicPort64 binPath=C:\\\\windows\\\\temp\\\\TVicPort64.sys type=kernel && sc.exe start TVicPort64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TVicPort64.sys"

# TVicPort64.sys

Load TVicPort64.sys kernel driver. Once loaded, device \\.\TVicPortDevice0 is accessible from any integrity level (no DACL). Send IOCTL 0x80002008 to map arbitrary physical memory into user-mode VA space via ZwMapViewOfSection and perform token stealing for LPE to SYSTEM.

**Use Case:** Arbitrary physical memory read/write from user mode. Exploitable from Low Integrity Level, Guest, or any AppContainer. Used for local privilege escalation to NT AUTHORITY\SYSTEM via token stealing, KASLR bypass, and kernel code execution.

**Required Privileges:** User (Low Integrity sufficient — no DACL on device object)

**MITRE ATT&CK:** T1068
