---
id: windows-kernel-inetcache
namespace: windows:kernel:inetcache
name: "inetcache.sys"
description: "inetcache.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create inetcache binPath=C:\\windows\\temp\\inetcache.sys type=kernel && sc.exe start inetcache"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load inetcache.sys kernel driver"
    commands:
      - "sc.exe create inetcache binPath=C:\\windows\\temp\\inetcache.sys type=kernel && sc.exe start inetcache"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create inetcache binPath=C:\\\\windows\\\\temp\\\\inetcache.sys type=kernel && sc.exe start inetcache"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver inetcache.sys"

# inetcache.sys

inetcache.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068