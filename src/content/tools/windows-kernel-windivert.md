---
id: windows-kernel-windivert
namespace: windows:kernel:windivert
name: "windivert.sys"
description: "WinDivert is a user-mode packet capture and network packet manipulation utility designed for Windows. It provides a powerful and flexible framework for intercepting, modifying, injecting, and dropping network packets at the network stack level. It operates as a lightweight, high-performance driver that interfaces directly with the network stack, allowing for detailed packet inspection and manipulation in real time."
author: "Michael Haag"
version: "1.0.0"
capabilities:
  - security.privilegeescalation.kernel-exploit
platforms:
  - windows
techniques:
  - privilege-escalation
risk_level: critical
trust_level: verified
execution:
  template: "sc.exe create windivert.sys binPath=C:\\windows\\temp\\windivert.sys type=kernel && sc.exe start windivert.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load windivert.sys kernel driver"
    commands:
      - "sc.exe create windivert.sys binPath=C:\\windows\\temp\\windivert.sys type=kernel && sc.exe start windivert.sys"
references:
  - label: "Reference"
    url: "https://www.3nailsinfosec.com/post/edrprison-borrow-a-legitimate-driver-to-mute-edr-agent"
  - label: "Reference"
    url: "https://github.com/basil00/WinDivert"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create windivert.sys binPath=C:\\\\windows\\\\temp\\\\windivert.sys type=kernel && sc.exe start windivert.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver windivert.sys"

# windivert.sys

WinDivert is a user-mode packet capture and network packet manipulation utility designed for Windows. It provides a powerful and flexible framework for intercepting, modifying, injecting, and dropping network packets at the network stack level. It operates as a lightweight, high-performance driver that interfaces directly with the network stack, allowing for detailed packet inspection and manipulation in real time.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068