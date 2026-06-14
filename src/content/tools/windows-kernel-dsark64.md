---
id: windows-kernel-dsark64
namespace: windows:kernel:dsark64
name: "DsArk64.sys"
description: "DsArk64.sys is a WHQL Microsoft-signed anti-rootkit kernel driver from Qihoo 360 Total Security. It exposes kernel-level process termination via ZwTerminateProcess from Ring 0 (kills PPL-protected processes), arbitrary kernel memory read (512 bytes), and arbitrary kernel memory write (32 bytes). The driver gates device access behind a custom Authenticode signing check that validates the calling process PE signature against Qihoo root certificates. This check is fully bypassed via process holl..."
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
  template: "sc.exe create DsArk binPath=C:\\windows\\temp\\DsArk64.sys type=kernel && sc.exe start DsArk"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load DsArk64.sys kernel driver"
    commands:
      - "sc.exe create DsArk binPath=C:\\windows\\temp\\DsArk64.sys type=kernel && sc.exe start DsArk"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/308"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create DsArk binPath=C:\\\\windows\\\\temp\\\\DsArk64.sys type=kernel && sc.exe start DsArk"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver DsArk64.sys"

# DsArk64.sys

DsArk64.sys is a WHQL Microsoft-signed anti-rootkit kernel driver from Qihoo 360 Total Security. It exposes kernel-level process termination via ZwTerminateProcess from Ring 0 (kills PPL-protected processes), arbitrary kernel memory read (512 bytes), and arbitrary kernel memory write (32 bytes). The driver gates device access behind a custom Authenticode signing check that validates the calling process PE signature against Qihoo root certificates. This check is fully bypassed via process hollowing into any Qihoo-signed executable (freely downloadable from 360.cn). The process kill IOCTL (0x80863008) requires no encryption or additional auth beyond the device open -- just a raw 4-byte PID. The kernel R/W IOCTLs use AES-128-CBC with a static key embedded in the binary. Initialization requires setting registry key HKLM\SYSTEM\CCS\Services\360FsFlt\daboot to 1.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068