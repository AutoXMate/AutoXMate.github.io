---
id: windows-kernel-asio
namespace: windows:kernel:asio
name: "asio.sys"
description: "Confirmed vulnerable driver from Microsoft Block List"
author: "Nasreddine Bencherchali, Michael Haag"
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
  template: "sc.exe create asio.sys binPath=C:\\windows\\temp\\asio.sys type=kernel && sc.exe start asio.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load asio.sys kernel driver"
    commands:
      - "sc.exe create asio.sys binPath=C:\\windows\\temp\\asio.sys type=kernel && sc.exe start asio.sys"
references:
  - label: "Reference"
    url: "https://github.com/namazso/physmem_drivers"
  - label: "Reference"
    url: "https://gist.github.com/mgraeber-rc/1bde6a2a83237f17b463d051d32e802c"
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/295"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create asio.sys binPath=C:\\\\windows\\\\temp\\\\asio.sys type=kernel && sc.exe start asio.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver asio.sys"

# asio.sys

Confirmed vulnerable driver from Microsoft Block List

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068