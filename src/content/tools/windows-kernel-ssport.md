---
id: windows-kernel-ssport
namespace: windows:kernel:ssport
name: "SSPORT.sys"
description: "Elevate privileges"
author: "Nasreddine Bencherchali"
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
  template: "sc.exe create SSPORT.sys binPath=C:\\windows\\temp\\SSPORT.sys     type=kernel && sc.exe start SSPORT.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load SSPORT.sys kernel driver"
    commands:
      - "sc.exe create SSPORT.sys binPath=C:\\windows\\temp\\SSPORT.sys     type=kernel && sc.exe start SSPORT.sys"
references:
  - label: "Reference"
    url: "https://github.com/VoidSec/Exploit-Development/tree/b82b6d3ac1cce66221101d3e0f4634aa64cb4ca7/windows/x64/kernel/ssport_v1.0"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SSPORT.sys binPath=C:\\\\windows\\\\temp\\\\SSPORT.sys     type=kernel && sc.exe start SSPORT.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SSPORT.sys"

# SSPORT.sys

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068