---
id: windows-kernel-stprocessmonitor
namespace: windows:kernel:stprocessmonitor
name: STProcessMonitor.sys
description: Safetica Technologies process monitoring kernel driver vulnerable to
  BYOVD-style process termination via IOCTL. CVE-2025-70795. 18 execution parents
  observed in VirusTotal indicating active abuse by threat actors. 1/73 detections.
  Driver facilitates arbitrary process kill from kernel context, enabling EDR/AV bypass.
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
  template: sc.exe create STProcessMonitor binPath=C:\windows\temp\STProcessMonitor.sys
    type=kernel && sc.exe start STProcessMonitor
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load STProcessMonitor.sys kernel driver
  commands:
  - sc.exe create STProcessMonitor binPath=C:\windows\temp\STProcessMonitor.sys type=kernel
    && sc.exe start STProcessMonitor
references:
- label: Reference
  url: https://www.cve.org/CVERecord?id=CVE-2025-70795
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/268
features:
- file-system
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
- stealth
- streaming
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create STProcessMonitor binPath=C:\\\\windows\\\\temp\\\\STProcessMonitor.sys type=kernel && sc.exe start STProcessMonitor"

# STProcessMonitor.sys

Safetica Technologies process monitoring kernel driver vulnerable to BYOVD-style process termination via IOCTL. CVE-2025-70795. 18 execution parents observed in VirusTotal indicating active abuse by threat actors. 1/73 detections. Driver facilitates arbitrary process kill from kernel context, enabling EDR/AV bypass.

**Use Case:** Disable security tools

**Required Privileges:** kernel

**MITRE ATT&CK:** T1562.001
