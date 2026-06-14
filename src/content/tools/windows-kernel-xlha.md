---
id: windows-kernel-xlha
namespace: windows:kernel:xlha
name: "XLHA.sys"
description: "XLHA.sys is a kernel driver from LG Electronics Inc. that exposes physical memory read/write via MmMapIoSpace and MSR read. Two other LG LHA.sys variants are already tracked in LOLDrivers. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository."
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
  template: "sc.exe create XLHA binPath=C:\\windows\\temp\\XLHA.sys type=kernel && sc.exe start XLHA"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load XLHA.sys kernel driver"
    commands:
      - "sc.exe create XLHA binPath=C:\\windows\\temp\\XLHA.sys type=kernel && sc.exe start XLHA"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/324"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create XLHA binPath=C:\\\\windows\\\\temp\\\\XLHA.sys type=kernel && sc.exe start XLHA"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver XLHA.sys"

# XLHA.sys

XLHA.sys is a kernel driver from LG Electronics Inc. that exposes physical memory read/write via MmMapIoSpace and MSR read. Two other LG LHA.sys variants are already tracked in LOLDrivers. The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068