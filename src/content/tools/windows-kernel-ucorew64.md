---
id: windows-kernel-ucorew64
namespace: windows:kernel:ucorew64
name: "UCOREW64.SYS"
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
trust_level: verified
execution:
  template: "sc.exe create UCOREW64.SYS binPath=C:\\windows\\temp\\UCOREW64.SYS type=kernel && sc.exe start UCOREW64.SYS"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load UCOREW64.SYS kernel driver"
    commands:
      - "sc.exe create UCOREW64.SYS binPath=C:\\windows\\temp\\UCOREW64.SYS type=kernel && sc.exe start UCOREW64.SYS"
references:
  - label: "Reference"
    url: "https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create UCOREW64.SYS binPath=C:\\\\windows\\\\temp\\\\UCOREW64.SYS type=kernel && sc.exe start UCOREW64.SYS"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver UCOREW64.SYS"

# UCOREW64.SYS

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068