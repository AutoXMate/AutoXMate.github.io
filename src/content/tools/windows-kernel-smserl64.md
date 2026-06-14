---
id: windows-kernel-smserl64
namespace: windows:kernel:smserl64
name: "SmSerl64.sys"
description: "A vulnerability exits in driver SmSerl64.sys in Motorola SM56 Modem WDM Driver v6.12.23.0, which allows low-privileged users to mapping physical memory via specially crafted IOCTL requests . This can be exploited for privilege escalation, code execution under high privileges, and information disclosure. These signed drivers can also be used to bypass the Microsoft driver-signing policy to deploy malicious code."
author: "valium"
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
  template: "sc.exe create SmSerl64.sys binPath=C:\\windows\\temp\\SmSerl64.sys type=kernel && sc.exe start SmSerl64.sys"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load SmSerl64.sys kernel driver"
    commands:
      - "sc.exe create SmSerl64.sys binPath=C:\\windows\\temp\\SmSerl64.sys type=kernel && sc.exe start SmSerl64.sys"
references:
  - label: "Reference"
    url: "https://nvd.nist.gov/vuln/detail/CVE-2024-55414"
  - label: "Reference"
    url: "https://github.com/heyheysky/vulnerable-driver/blob/master/CVE-2024-55414/CVE-2024-55414_SmSerl64.sys_README.md"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create SmSerl64.sys binPath=C:\\\\windows\\\\temp\\\\SmSerl64.sys type=kernel && sc.exe start SmSerl64.sys"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver SmSerl64.sys"

# SmSerl64.sys

A vulnerability exits in driver SmSerl64.sys in Motorola SM56 Modem WDM Driver v6.12.23.0, which allows low-privileged users to mapping physical memory via specially crafted IOCTL requests . This can be exploited for privilege escalation, code execution under high privileges, and information disclosure. These signed drivers can also be used to bypass the Microsoft driver-signing policy to deploy malicious code.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068