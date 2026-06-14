---
id: windows-kernel-netproxydriver
namespace: windows:kernel:netproxydriver
name: "NetProxyDriver.sys"
description: "Elevate privileges"
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: high
trust_level: community
execution:
  template: "sc.exe create NetProxyDriver.sys binPath=C:\\windows\\temp\\NetProxyDriver.sys     type=kernel type=kernel && sc.exe start NetProxyDriver.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load NetProxyDriver.sys kernel driver"
    commands:
      - "sc.exe create NetProxyDriver.sys binPath=C:\\windows\\temp\\NetProxyDriver.sys     type=kernel type=kernel && sc.exe start NetProxyDriver.sys"
references:
  - label: "Reference"
    url: "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create NetProxyDriver.sys binPath=C:\\\\windows\\\\temp\\\\NetProxyDriver.sys     type=kernel type=kernel && sc.exe start NetProxyDriver.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver NetProxyDriver.sys"

# NetProxyDriver.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068