---
id: windows-kernel-cormem
namespace: windows:kernel:cormem
name: "CorMem.sys"
description: "Teledyne Digital Imaging CorMem.sys (Sapera Memory Manager) exposes physical memory read/write, contiguous memory allocation, and I/O port access to user-mode processes via CorMem.dll wrapper functions. The driver provides 36 exported functions including CorMemGetPhysMemory, CorMemMapPhysMemory, CorMemAllocPhysMemory, CorMemReadIo, and CorMemWriteIo. Actively abused for BYOVD with 0/71 VT detection. Execution parents include Cobalt Strike/IcedID malware and game cheat kernel loaders."
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
  template: "sc.exe create CorMem.sys binPath=C:\\windows\\temp\\CorMem.sys type=kernel && sc.exe start CorMem.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load CorMem.sys kernel driver"
    commands:
      - "sc.exe create CorMem.sys binPath=C:\\windows\\temp\\CorMem.sys type=kernel && sc.exe start CorMem.sys"
references:
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/cormem.sys-vulnerable-driver"
  - label: "Reference"
    url: "https://www.virustotal.com/gui/file/40c855d20d497823716a08a443dc85846233226985ee653770bc3b245cf2ed0f"
  - label: "Reference"
    url: "https://x.com/skept1kal/status/2040200734570877354"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CorMem.sys binPath=C:\\\\windows\\\\temp\\\\CorMem.sys type=kernel && sc.exe start CorMem.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CorMem.sys"

# CorMem.sys

Teledyne Digital Imaging CorMem.sys (Sapera Memory Manager) exposes physical memory read/write, contiguous memory allocation, and I/O port access to user-mode processes via CorMem.dll wrapper functions. The driver provides 36 exported functions including CorMemGetPhysMemory, CorMemMapPhysMemory, CorMemAllocPhysMemory, CorMemReadIo, and CorMemWriteIo. Actively abused for BYOVD with 0/71 VT detection. Execution parents include Cobalt Strike/IcedID malware and game cheat kernel loaders.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068