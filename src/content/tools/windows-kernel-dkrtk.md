---
id: windows-kernel-dkrtk
namespace: windows:kernel:dkrtk
name: dkrTK.sys
description: The User Agent tjr.exe, which is protected via a virtual machine, drops
  the kernel driver to the user temporary directory C:\%User%\AppData\Local\Temp\Ktgn.sys.
  It then installs the dropped driver with the name ktgn and the start value = System
  (to start when the system restarts). From our analysis of what occurs when a user
  interfaces with this driver, we observed that it only uses one of the exposed Device
  Input and Output Control (IOCTL) code — Kill Process, which is used to kill security
  ...
author: Will BushidoToken
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
  template: sc.exe create dkrTK.sys binPath=C:\windows\temp\dkrTK.sys type=kernel
    && sc.exe start dkrTK.sys
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dkrTK.sys kernel driver
  commands:
  - sc.exe create dkrTK.sys binPath=C:\windows\temp\dkrTK.sys type=kernel && sc.exe
    start dkrTK.sys
references:
- label: Reference
  url: https://www.trendmicro.com/content/dam/trendmicro/global/en/research/23/e/blackcat-ransomware-deploys-new-signed-kernel-driver/indicators-blackcat-ransomware-deploys-new-signed-kernel-driver.txt
- label: Reference
  url: https://www.trendmicro.com/en_us/research/23/e/blackcat-ransomware-deploys-new-signed-kernel-driver.html
features:
- compression
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dkrTK.sys binPath=C:\\\\windows\\\\temp\\\\dkrTK.sys type=kernel && sc.exe start dkrTK.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dkrTK.sys"

# dkrTK.sys

The User Agent tjr.exe, which is protected via a virtual machine, drops the kernel driver to the user temporary directory C:\%User%\AppData\Local\Temp\Ktgn.sys. It then installs the dropped driver with the name ktgn and the start value = System (to start when the system restarts). From our analysis of what occurs when a user interfaces with this driver, we observed that it only uses one of the exposed Device Input and Output Control (IOCTL) code — Kill Process, which is used to kill security agent processes installed on the system.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
