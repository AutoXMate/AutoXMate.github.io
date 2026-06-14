---
id: windows-kernel-energydriver
namespace: windows:kernel:energydriver
name: "energydriver.sys"
description: "EnergyDriver.sys is a kernel driver from Intel Corporation shipped with Intel Power Gadget 3.6 (deprecated December 2023). The driver exposes 5 IOCTLs including arbitrary wrmsr (any MSR index, any 64-bit value, no whitelist), arbitrary rdmsr (single CPU or all CPUs), and arbitrary physical memory read via MmMapIoSpace. wrmsr allows IA32_LSTAR hijack for direct syscall redirection. No privilege check, no MSR whitelist, default DACL. WHQL and Intel EV dual-signed."
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
  template: "sc.exe create energydriver binPath=C:\\windows\\temp\\energydriver.sys type=kernel && sc.exe start energydriver"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load energydriver.sys kernel driver"
    commands:
      - "sc.exe create energydriver binPath=C:\\windows\\temp\\energydriver.sys type=kernel && sc.exe start energydriver"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/329"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create energydriver binPath=C:\\\\windows\\\\temp\\\\energydriver.sys type=kernel && sc.exe start energydriver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver energydriver.sys"

# energydriver.sys

EnergyDriver.sys is a kernel driver from Intel Corporation shipped with Intel Power Gadget 3.6 (deprecated December 2023). The driver exposes 5 IOCTLs including arbitrary wrmsr (any MSR index, any 64-bit value, no whitelist), arbitrary rdmsr (single CPU or all CPUs), and arbitrary physical memory read via MmMapIoSpace. wrmsr allows IA32_LSTAR hijack for direct syscall redirection. No privilege check, no MSR whitelist, default DACL. WHQL and Intel EV dual-signed.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068