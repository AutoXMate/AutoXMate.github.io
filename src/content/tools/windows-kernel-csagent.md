---
id: windows-kernel-csagent
namespace: windows:kernel:csagent
name: CSAgent.sys
description: AbyssWorker rootkit masquerading as a CrowdStrike Falcon sensor driver
  (CSAgent.sys). Signed with a revoked certificate from Shenzhen yundian Technology
  Co., Ltd. This is a fully malicious driver that blinds security products by stripping
  handles, terminating processes, and removing notification callbacks. Identified
  in ESET EDR killers research (March 2026) deployed alongside Medusa ransomware via
  the HEARTCRYPT packer.
author: Michael Haag
version: 1.0.0
capabilities:
- security.privilegeescalation.kernel-exploit
platforms:
- windows
techniques:
- privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: sc.exe create CSAgent.sys binPath=C:\windows\temp\CSAgent.sys type=kernel
    && sc.exe start CSAgent.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load CSAgent.sys kernel driver
  commands:
  - sc.exe create CSAgent.sys binPath=C:\windows\temp\CSAgent.sys type=kernel && sc.exe
    start CSAgent.sys
references:
- label: Reference
  url: https://www.welivesecurity.com/en/eset-research/edr-killers-explained/
features:
- encryption
- file-system
- network-intensive
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create CSAgent.sys binPath=C:\\\\windows\\\\temp\\\\CSAgent.sys type=kernel && sc.exe start CSAgent.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver CSAgent.sys"

# CSAgent.sys

AbyssWorker rootkit masquerading as a CrowdStrike Falcon sensor driver (CSAgent.sys). Signed with a revoked certificate from Shenzhen yundian Technology Co., Ltd. This is a fully malicious driver that blinds security products by stripping handles, terminating processes, and removing notification callbacks. Identified in ESET EDR killers research (March 2026) deployed alongside Medusa ransomware via the HEARTCRYPT packer.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1014

**Variants:** 4 known variants
