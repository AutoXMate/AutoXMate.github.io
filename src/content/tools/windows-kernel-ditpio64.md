---
id: windows-kernel-ditpio64
namespace: windows:kernel:ditpio64
name: ditpio64.sys
description: ditpio64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers
  repository. The driver exposes dangerous kernel primitives to usermode.
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
  template: sc.exe create ditpio64 binPath=C:\windows\temp\ditpio64.sys type=kernel
    && sc.exe start ditpio64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load ditpio64.sys kernel driver
  commands:
  - sc.exe create ditpio64 binPath=C:\windows\temp\ditpio64.sys type=kernel && sc.exe
    start ditpio64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/325
- label: Reference
  url: https://github.com/KeServiceDescriptorTable/vulnerable-drivers
features:
- file-system
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ditpio64 binPath=C:\\\\windows\\\\temp\\\\ditpio64.sys type=kernel && sc.exe start ditpio64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ditpio64.sys"

# ditpio64.sys

ditpio64.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
