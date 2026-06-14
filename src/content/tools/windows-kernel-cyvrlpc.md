---
id: windows-kernel-cyvrlpc
namespace: windows:kernel:cyvrlpc
name: cyvrlpc.sys
description: Per Sophos X-Ops research (Aug 06, 2025), threat actors deploy an EDR-killer
  that loads a malicious kernel driver (often with a random five-letter name) signed
  with compromised or revoked code-signing certificates (e.g., Changsha Hengxiang
  Information Technology; Fuzhou Dingxin Trade). The tool targets many security products
  by killing their services and processes and is frequently distributed packed with
  HeartCrypt by ransomware groups (e.g., RansomHub, INC). Driver names are hard-coded
  per ...
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
  template: sc.exe create cyvrlpc.sys binPath=C:\windows\temp\cyvrlpc.sys type=kernel
    && sc.exe start cyvrlpc.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load cyvrlpc.sys kernel driver
  commands:
  - sc.exe create cyvrlpc.sys binPath=C:\windows\temp\cyvrlpc.sys type=kernel && sc.exe
    start cyvrlpc.sys
references:
- label: Reference
  url: https://news.sophos.com/en-us/2025/08/06/shared-secret-edr-killer-in-the-kill-chain/
features:
- compression
- encryption
- file-system
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create cyvrlpc.sys binPath=C:\\\\windows\\\\temp\\\\cyvrlpc.sys type=kernel && sc.exe start cyvrlpc.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver cyvrlpc.sys"

# cyvrlpc.sys

Per Sophos X-Ops research
(Aug 06, 2025), threat actors deploy an EDR-killer that loads a malicious
kernel driver (often with a random five-letter name) signed with
compromised or revoked code-signing certificates (e.g., Changsha Hengxiang
Information Technology; Fuzhou Dingxin Trade). The tool targets many
security products by killing their services and processes and is frequently
distributed packed with HeartCrypt by ransomware groups (e.g., RansomHub,
INC). Driver names are hard-coded per sample (e.g., mraml.sys, noedt.sys).


**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
