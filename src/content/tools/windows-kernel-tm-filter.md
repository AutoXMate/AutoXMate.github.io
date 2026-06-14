---
id: windows-kernel-tm-filter
namespace: windows:kernel:tm-filter
name: tm_filter.sys
description: Teramind Inc. kernel-mode filter drivers (tm_filter.sys and tmfsdrv2.sys)
  providing kernel-level input capture including keylogging and screen capture capabilities.
  Both signed by DigiCert under Teramind Inc. certificate. Execution parents point
  to teramind_agent MSI installer. Abused by threat actors for stealth monitoring
  operations. tmfsdrv2.sys has 1/73 detections on VirusTotal.
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
  template: sc.exe create tmfsdrv2 binPath=C:\windows\temp\tmfsdrv2.sys type=kernel
    && sc.exe start tmfsdrv2
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load tm_filter.sys kernel driver
  commands:
  - sc.exe create tmfsdrv2 binPath=C:\windows\temp\tmfsdrv2.sys type=kernel && sc.exe
    start tmfsdrv2
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/243
features:
- encryption
- interactive
- pipes-stdin
- pipes-stdout
- requires-root
- stealth
- streaming
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create tmfsdrv2 binPath=C:\\\\windows\\\\temp\\\\tmfsdrv2.sys type=kernel && sc.exe start tmfsdrv2"

# tm_filter.sys

Teramind Inc. kernel-mode filter drivers (tm_filter.sys and tmfsdrv2.sys) providing kernel-level input capture including keylogging and screen capture capabilities. Both signed by DigiCert under Teramind Inc. certificate. Execution parents point to teramind_agent MSI installer. Abused by threat actors for stealth monitoring operations. tmfsdrv2.sys has 1/73 detections on VirusTotal.

**Use Case:** Capture user input and screen content for surveillance

**Required Privileges:** kernel

**MITRE ATT&CK:** T1056.001
