---
id: windows-kernel-uddb2b6
namespace: windows:kernel:uddb2b6
name: UDDB2B6.sys
description: UDDB2B6.sys is a TechPowerUp kernel driver (GPU-Z variant) that exposes
  I/O port read/write, MSR read/write, MmMapIoSpace map/unmap/read/write, and PCI
  configuration space read/write. TechPowerUp has a history of vulnerable kernel drivers
  including GPU-Z.sys (CVE-2019-7245, CVE-2025-5324) and ThrottleStop.sys (CVE-2025-7771).
  The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.
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
  template: sc.exe create UDDB2B6 binPath=C:\windows\temp\UDDB2B6.sys type=kernel
    && sc.exe start UDDB2B6
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load UDDB2B6.sys kernel driver
  commands:
  - sc.exe create UDDB2B6 binPath=C:\windows\temp\UDDB2B6.sys type=kernel && sc.exe
    start UDDB2B6
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/323
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- network-intensive
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create UDDB2B6 binPath=C:\\\\windows\\\\temp\\\\UDDB2B6.sys type=kernel && sc.exe start UDDB2B6"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver UDDB2B6.sys"

# UDDB2B6.sys

UDDB2B6.sys is a TechPowerUp kernel driver (GPU-Z variant) that exposes I/O port read/write, MSR read/write, MmMapIoSpace map/unmap/read/write, and PCI configuration space read/write. TechPowerUp has a history of vulnerable kernel drivers including GPU-Z.sys (CVE-2019-7245, CVE-2025-5324) and ThrottleStop.sys (CVE-2025-7771). The driver is available in the KeServiceDescriptorTable/vulnerable-drivers repository.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
