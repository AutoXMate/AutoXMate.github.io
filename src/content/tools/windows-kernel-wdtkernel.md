---
id: windows-kernel-wdtkernel
namespace: windows:kernel:wdtkernel
name: "WDTKernel.sys"
description: "WDTKernel.sys is a Dell Watchdog Timer Kernel Driver that exposes 12 IOCTLs for arbitrary physical memory read/write via MmMapIoSpace with zero validation on user-supplied physical addresses. It also provides 12 IOCTLs for unrestricted I/O port access and 2 IOCTLs for PCI configuration space access. The driver was WHQL attestation signed through Microsoft and is distributed via the Microsoft Update Catalog. VMware Carbon Black TAU mentioned this driver in their October 2023 research but class..."
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
  template: "sc.exe create WDTKernel binPath=C:\\windows\\temp\\WDTKernel.sys type=kernel && sc.exe start WDTKernel"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load WDTKernel.sys kernel driver"
    commands:
      - "sc.exe create WDTKernel binPath=C:\\windows\\temp\\WDTKernel.sys type=kernel && sc.exe start WDTKernel"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/290"
  - label: "Reference"
    url: "https://blogs.vmware.com/security/2023/10/hunting-vulnerable-kernel-drivers.html"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create WDTKernel binPath=C:\\\\windows\\\\temp\\\\WDTKernel.sys type=kernel && sc.exe start WDTKernel"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver WDTKernel.sys"

# WDTKernel.sys

WDTKernel.sys is a Dell Watchdog Timer Kernel Driver that exposes 12 IOCTLs for arbitrary physical memory read/write via MmMapIoSpace with zero validation on user-supplied physical addresses. It also provides 12 IOCTLs for unrestricted I/O port access and 2 IOCTLs for PCI configuration space access. The driver was WHQL attestation signed through Microsoft and is distributed via the Microsoft Update Catalog. VMware Carbon Black TAU mentioned this driver in their October 2023 research but classified it as not vulnerable in terms of access control because its INF sets an SDDL restricting device access to Administrators and SYSTEM. The arbitrary physical memory R/W via MmMapIoSpace was not analyzed or documented by TAU. Device path is \\.\__WDT__. Suitable for BYOVD attacks where the attacker already has admin privileges and needs kernel-level memory access to bypass EDR.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068