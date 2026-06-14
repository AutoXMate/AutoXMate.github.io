---
id: windows-kernel-isodrivep64
namespace: windows:kernel:isodrivep64
name: isodrivep64.sys
description: ABYSSWORKER is a malicious driver used in MEDUSA ransomware attacks to
  disable EDR systems. The driver masquerades as a legitimate CrowdStrike Falcon driver
  and provides extensive capabilities to terminate processes, remove security callbacks,
  manipulate files, and disable security tools. It uses stolen certificates from Chinese
  companies and requires a specific password for activation. The driver was observed
  being deployed alongside HEARTCRYPT-packed loaders and provides attackers with kern...
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
  template: sc.exe create isodrivep64.sys binPath=C:\windows\temp\isodrivep64.sys
    type=kernel && sc.exe start isodrivep64.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load isodrivep64.sys kernel driver
  commands:
  - sc.exe create isodrivep64.sys binPath=C:\windows\temp\isodrivep64.sys type=kernel
    && sc.exe start isodrivep64.sys
references:
- label: Reference
  url: https://www.elastic.co/security-labs/abyssworker
features:
- encryption
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create isodrivep64.sys binPath=C:\\\\windows\\\\temp\\\\isodrivep64.sys type=kernel && sc.exe start isodrivep64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver isodrivep64.sys"

# isodrivep64.sys

ABYSSWORKER is a malicious driver used in MEDUSA ransomware attacks to disable EDR systems. The driver masquerades as a legitimate CrowdStrike Falcon driver and provides extensive capabilities to terminate processes, remove security callbacks, manipulate files, and disable security tools. It uses stolen certificates from Chinese companies and requires a specific password for activation. The driver was observed being deployed alongside HEARTCRYPT-packed loaders and provides attackers with kernel-level capabilities to blind EDR products by removing notification callbacks, detaching mini-filter devices, and replacing driver major functions.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068

**Variants:** 2 known variants
