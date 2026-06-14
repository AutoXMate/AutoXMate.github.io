---
id: windows-kernel-irec
namespace: windows:kernel:irec
name: "irec.sys"
description: "The driver in question, identified as \\\\.\\IREC, provides an interface for external programs to directly interact with system processes. Its key functionality is encapsulated in the OPENPROCESS function which, upon receiving a Process ID (PID), returns a handle to that specific process operating within the kernels domain. The vulnerability emerges from the indiscriminate nature of this functionality. An ill-intentioned actor can exploit this to obtain handles to critical processes like LSASS. ..."
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
  template: "sc.exe create irec binPath=C:\\windows\\temp\\irec.sys type=kernel && sc.exe start irec.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load irec.sys kernel driver"
    commands:
      - "sc.exe create irec binPath=C:\\windows\\temp\\irec.sys type=kernel && sc.exe start irec.sys"
references:
  - label: "Reference"
    url: "https://blog.dru1d.ninja/windows-driver-exploit-development-irec-sys-a5eb45093945"
  - label: "Reference"
    url: "https://gist.github.com/dru1d-foofus/1af21179f253879f101c3a8d4f718bf0"
  - label: "Reference"
    url: "https://www.binalyze.com/irec"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create irec binPath=C:\\\\windows\\\\temp\\\\irec.sys type=kernel && sc.exe start irec.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver irec.sys"

# irec.sys

The driver in question, identified as \\.\IREC, provides an interface for external programs to directly interact with system processes. Its key functionality is encapsulated in the OPENPROCESS function which, upon receiving a Process ID (PID), returns a handle to that specific process operating within the kernels domain. The vulnerability emerges from the indiscriminate nature of this functionality. An ill-intentioned actor can exploit this to obtain handles to critical processes like LSASS. With a hardcoded access mask of 0x410, this driver essentially grants PROCESS_QUERY_INFORMATION and PROCESS_VM_READ permissions, enabling unauthorized memory dumps from privileged processes, all from an unprivileged context.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068