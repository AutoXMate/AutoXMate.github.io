---
id: windows-kernel-biontdrv
namespace: windows:kernel:biontdrv
name: BioNTdrv.sys
description: Microsoft has identified five security flaws in the Paragon Partition
  Manager BioNTdrv.sys driver, one of which was exploited by ransomware gangs in zero-day
  attacks to gain SYSTEM privileges on Windows systems. These vulnerabilities, found
  in BioNTdrv.sys versions 1.3.0 and 1.5.1, enable attackers to escalate their privileges
  to SYSTEM level to a higher access level than standard administrator permissions.
author: Swachchhanda Shrawan Poudel
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
  template: sc.exe create BioNTdrv.sys binPath=C:\windows\temp\BioNTdrv.sys type=kernel
    && sc.exe start BioNTdrv.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load BioNTdrv.sys kernel driver
  commands:
  - sc.exe create BioNTdrv.sys binPath=C:\windows\temp\BioNTdrv.sys type=kernel &&
    sc.exe start BioNTdrv.sys
references:
- label: Reference
  url: https://www.sdxcentral.com/alerts/paragon-partition-manager-driver-flaws-enable-privilege-escalation-and-dos-attacks/2025/02/
- label: Reference
  url: https://www.bleepingcomputer.com/news/security/ransomware-gangs-exploit-paragon-partition-manager-bug-in-byovd-attacks/
- label: Reference
  url: https://paragon-software.zendesk.com/hc/en-us/articles/32993902732817-IMPORTANT-Paragon-Driver-Security-Patch-for-All-Products-of-Hard-Disk-Manager-Product-Line-Biontdrv-sys
features:
- file-system
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BioNTdrv.sys binPath=C:\\\\windows\\\\temp\\\\BioNTdrv.sys type=kernel && sc.exe start BioNTdrv.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver BioNTdrv.sys"

# BioNTdrv.sys

Microsoft has identified five security flaws in the Paragon Partition Manager BioNTdrv.sys driver, one of which was exploited by ransomware gangs in zero-day attacks to gain SYSTEM privileges on Windows systems. These vulnerabilities, found in BioNTdrv.sys versions 1.3.0 and 1.5.1, enable attackers to escalate their privileges to SYSTEM level to a higher access level than standard administrator permissions.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
