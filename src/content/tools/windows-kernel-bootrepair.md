---
id: windows-kernel-bootrepair
namespace: windows:kernel:bootrepair
name: "bootrepair.sys"
description: "BootRepair.sys is a legitimate Lenovo kernel driver shipped with Lenovo PC Manager (signed by LENOVO via Symantec Class 3 SHA256 Code Signing CA, compile date 2018-01-03). The driver creates a device object at \\\\.\\BootRepair with no DACL restrictions, so any local user can open a handle. The IRP_MJ_DEVICE_CONTROL dispatcher accepts IOCTL 0x222014 with a 4-byte DWORD input (target PID) and chains PsLookupProcessByProcessId -> ObOpenObjectByPointer -> ZwTerminateProcess against the supplied PID..."
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
  template: "sc.exe create BootRepair binPath=C:\\windows\\temp\\BootRepair.sys type=kernel && sc.exe start BootRepair"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load bootrepair.sys kernel driver"
    commands:
      - "sc.exe create BootRepair binPath=C:\\windows\\temp\\BootRepair.sys type=kernel && sc.exe start BootRepair"
references:
  - label: "Reference"
    url: "https://medium.com/@jehadbudagga/phantom-killer-reverse-engineering-and-weaponizing-a-lenovo-driver-to-terminate-edr-processes-9191cd06374f"
  - label: "Reference"
    url: "https://github.com/redteamfortress/PhantomKiller"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create BootRepair binPath=C:\\\\windows\\\\temp\\\\BootRepair.sys type=kernel && sc.exe start BootRepair"

# bootrepair.sys

BootRepair.sys is a legitimate Lenovo kernel driver shipped with Lenovo PC Manager (signed by LENOVO via Symantec Class 3 SHA256 Code Signing CA, compile date 2018-01-03). The driver creates a device object at \\.\BootRepair with no DACL restrictions, so any local user can open a handle. The IRP_MJ_DEVICE_CONTROL dispatcher accepts IOCTL 0x222014 with a 4-byte DWORD input (target PID) and chains PsLookupProcessByProcessId -> ObOpenObjectByPointer -> ZwTerminateProcess against the supplied PID, with no caller validation. Because the kernel-mode caller bypasses user-mode access checks, the primitive can terminate any process on the system including PPL-protected AV/EDR processes. The driver also imports ZwCreateKey / ZwSetValueKey / ZwQueryValueKey (registry access for the boot-repair feature), PsCreateSystemThread / IoRegisterShutdownNotification, and KeBugCheckEx.

**Use Case:** Terminate arbitrary processes from kernel mode (including PPL-protected AV/EDR processes) via an unauthenticated IOCTL handler.

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068