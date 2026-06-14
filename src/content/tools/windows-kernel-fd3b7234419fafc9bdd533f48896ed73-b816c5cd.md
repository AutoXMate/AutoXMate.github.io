---
id: windows-kernel-fd3b7234419fafc9bdd533f48896ed73-b816c5cd
namespace: windows:kernel:fd3b7234419fafc9bdd533f48896ed73-b816c5cd
name: fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys
description: The criminals signed their AV-killer malware, closely related to one
  known as BURNTCIGAR, with a legitimate WHCP certificate
author: Viral Maniar
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
  template: sc.exe create fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys binPath=C:\windows\temp\fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys
    type=kernel && sc.exe start fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys kernel driver
  commands:
  - sc.exe create fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys binPath=C:\windows\temp\fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys
    type=kernel && sc.exe start fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys
references:
- label: Reference
  url: https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/114
features:
- encryption
- file-system
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys binPath=C:\\\\windows\\\\temp\\\\fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys type=kernel && sc.exe start fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys"

# fd3b7234419fafc9bdd533f48896ed73_b816c5cd.sys

The criminals signed their AV-killer malware, closely related to one known as BURNTCIGAR, with a legitimate WHCP certificate

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
