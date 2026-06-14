---
id: windows-kernel-immunetutildriver
namespace: windows:kernel:immunetutildriver
name: "ImmunetUtilDriver.sys"
description: "ImmunetUtilDriver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode."
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
  template: "sc.exe create ImmunetUtilDriver binPath=C:\\windows\\temp\\ImmunetUtilDriver.sys type=kernel && sc.exe start ImmunetUtilDriver"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load ImmunetUtilDriver.sys kernel driver"
    commands:
      - "sc.exe create ImmunetUtilDriver binPath=C:\\windows\\temp\\ImmunetUtilDriver.sys type=kernel && sc.exe start ImmunetUtilDriver"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/325"
  - label: "Reference"
    url: "https://github.com/KeServiceDescriptorTable/vulnerable-drivers"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create ImmunetUtilDriver binPath=C:\\\\windows\\\\temp\\\\ImmunetUtilDriver.sys type=kernel && sc.exe start ImmunetUtilDriver"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver ImmunetUtilDriver.sys"

# ImmunetUtilDriver.sys

ImmunetUtilDriver.sys is a vulnerable kernel driver from the KeServiceDescriptorTable/vulnerable-drivers repository. The driver exposes dangerous kernel primitives to usermode.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068