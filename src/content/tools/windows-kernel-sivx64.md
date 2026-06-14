---
id: windows-kernel-sivx64
namespace: windows:kernel:sivx64
name: "SIVX64.sys"
description: "Ray Hinchliffe SIV (System Information Viewer) SIVX64.sys v5.85 dynamically resolves MmMapIoSpace and MmMapIoSpaceEx via MmGetSystemRoutineAddress at runtime (neither appears in the IAT), evading static import-based scanning. The driver exposes multiple privileged IOCTL primitives via \\\\.\\SIVDRIVER including arbitrary physical memory mapped read/write (Cmd 0x14, critical), physical memory read via scatter-gather (Cmd 0x10) and bulk MDL (Cmd 0x13), MSR read/write on a whitelisted subset (Cmd 0..."
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
  template: "sc.exe create SIVDRIVER binPath=C:\\windows\\temp\\SIVX64.sys type=kernel && sc.exe start SIVDRIVER"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load SIVX64.sys kernel driver"
    commands:
      - "sc.exe create SIVDRIVER binPath=C:\\windows\\temp\\SIVX64.sys type=kernel && sc.exe start SIVDRIVER"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/287"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/33903e8fa9f0a2acaa4784d645e309b0bd780693824b6c2c5fef257238c77478"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SIVDRIVER binPath=C:\\\\windows\\\\temp\\\\SIVX64.sys type=kernel && sc.exe start SIVDRIVER"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SIVX64.sys"

# SIVX64.sys

Ray Hinchliffe SIV (System Information Viewer) SIVX64.sys v5.85 dynamically resolves MmMapIoSpace and MmMapIoSpaceEx via MmGetSystemRoutineAddress at runtime (neither appears in the IAT), evading static import-based scanning. The driver exposes multiple privileged IOCTL primitives via \\.\SIVDRIVER including arbitrary physical memory mapped read/write (Cmd 0x14, critical), physical memory read via scatter-gather (Cmd 0x10) and bulk MDL (Cmd 0x13), MSR read/write on a whitelisted subset (Cmd 0x08/0x0C), unrestricted I/O port read/scan (Cmd 0x44/0x50), and unrestricted PCI configuration space read (Cmd 0x48). WHQL signed by Microsoft Windows Hardware Compatibility Publisher; loads despite HVCI.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068