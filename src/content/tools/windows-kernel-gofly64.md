---
id: windows-kernel-gofly64
namespace: windows:kernel:gofly64
name: GoFly64.sys
description: GoFly64.sys is a WFP (Windows Filtering Platform) network filter driver
  signed by a Chinese software company (南京偲言睿网络科技有限公司 / Nanjing Siyanrui Network Technology)
  that exposes 20+ IOCTLs to usermode with no authentication. The most critical primitive
  is IOCTL 0x12227A which opens any process by PID via ZwOpenProcess and terminates
  it via ZwTerminateProcess, enabling kernel-level EDR/AV process killing. Additional
  capabilities include WFP-based network traffic interception and packet injection...
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
  template: sc.exe create GoFly64 binPath=C:\windows\temp\GoFly64.sys type=kernel
    && sc.exe start GoFly64
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load GoFly64.sys kernel driver
  commands:
  - sc.exe create GoFly64 binPath=C:\windows\temp\GoFly64.sys type=kernel && sc.exe
    start GoFly64
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/299
features:
- file-system
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
- requires-root
- stealth
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create GoFly64 binPath=C:\\\\windows\\\\temp\\\\GoFly64.sys type=kernel && sc.exe start GoFly64"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver GoFly64.sys"

# GoFly64.sys

GoFly64.sys is a WFP (Windows Filtering Platform) network filter driver signed by a Chinese software company (南京偲言睿网络科技有限公司 / Nanjing Siyanrui Network Technology) that exposes 20+ IOCTLs to usermode with no authentication. The most critical primitive is IOCTL 0x12227A which opens any process by PID via ZwOpenProcess and terminates it via ZwTerminateProcess, enabling kernel-level EDR/AV process killing. Additional capabilities include WFP-based network traffic interception and packet injection (FwpsInjectNetworkSendAsync, FwpsInjectNetworkReceiveAsync), IPv4 traffic redirection (IOCTL 0x122262 via RtlIpv4StringToAddressA), process creation monitoring (PsSetCreateProcessNotifyRoutineEx), image load monitoring (PsSetLoadImageNotifyRoutine), and kernel-mode file write operations. VT shows 88 malicious execution parents including malware droppers and PowerShell scripts, confirming heavy abuse in the wild for BYOVD attacks. Also distributed as PandaSpeed64.sys and drv_02581.sys.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
