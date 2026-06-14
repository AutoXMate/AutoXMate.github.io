---
id: windows-kernel-trixx
namespace: windows:kernel:trixx
name: "TRIXX.sys"
description: "TRIXX.sys is a shared utility kernel driver distributed by TechPowerUp LLC with Sapphire TRIXX and GPU-Z. The driver provides completely unrestricted hardware access from usermode through 16+ IOCTLs with zero validation on hardware parameters, including arbitrary port I/O read/write, arbitrary PCI configuration space read/write via HalGetBusDataByOffset/HalSetBusDataByOffset, MMIO BAR mapping via MmMapIoSpace, and MMIO read/write through mapped BARs. Physical memory read/write is achievable b..."
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
  template: "sc.exe create TRIXX binPath=C:\\windows\\temp\\TRIXX.sys type=kernel && sc.exe start TRIXX"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load TRIXX.sys kernel driver"
    commands:
      - "sc.exe create TRIXX binPath=C:\\windows\\temp\\TRIXX.sys type=kernel && sc.exe start TRIXX"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/291"
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/320"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create TRIXX binPath=C:\\\\windows\\\\temp\\\\TRIXX.sys type=kernel && sc.exe start TRIXX"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver TRIXX.sys"

# TRIXX.sys

TRIXX.sys is a shared utility kernel driver distributed by TechPowerUp LLC with Sapphire TRIXX and GPU-Z. The driver provides completely unrestricted hardware access from usermode through 16+ IOCTLs with zero validation on hardware parameters, including arbitrary port I/O read/write, arbitrary PCI configuration space read/write via HalGetBusDataByOffset/HalSetBusDataByOffset, MMIO BAR mapping via MmMapIoSpace, and MMIO read/write through mapped BARs. Physical memory read/write is achievable by remapping a PCI device BAR to a target physical address then mapping it via MmMapIoSpace. The driver creates its device dynamically based on the Windows service name and has no hardware dependency, loading on any x64 Windows system. TechPowerUp has a history of vulnerable kernel drivers including GPU-Z.sys (CVE-2019-7245, CVE-2025-5324) and ThrottleStop.sys (CVE-2025-7771) which expose the same MmMapIoSpace primitive. Fresh EV code signing certificate valid until April 2028 with zero AV detections.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068