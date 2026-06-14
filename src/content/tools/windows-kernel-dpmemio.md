---
id: windows-kernel-dpmemio
namespace: windows:kernel:dpmemio
name: dpmemio.sys
description: ET&T Technology Co., Ltd. dpmemio.sys (ClevoECView) is a 12KB driver
  with only 9 imports that provides completely unrestricted arbitrary physical memory
  read/write and I/O port access with no authentication, no ACL, no address validation,
  and no size validation. MmUnmapIoSpace is not even imported, meaning every MmMapIoSpace
  call permanently leaks a system PTE mapping. An additional bug exists where MOVSXD
  sign-extension on a 32-bit UserBufferPtr provides a write-to-kernel-VA primitive.
  IOCTL...
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
  template: sc.exe create dpMemIO binPath=C:\windows\temp\dpmemio.sys type=kernel
    && sc.exe start dpMemIO
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load dpmemio.sys kernel driver
  commands:
  - sc.exe create dpMemIO binPath=C:\windows\temp\dpmemio.sys type=kernel && sc.exe
    start dpMemIO
references:
- label: Reference
  url: https://github.com/magicsword-io/LOLDrivers/issues/288
- label: Reference
  url: https://www.virustotal.com/gui/file/7cf6881e43337c288b1883fafb234146a450ff94388aee395e05e36202c5afbb
- label: Reference
  url: https://www.virustotal.com/gui/file/cd631c54fe1375e4bdd2f63b58bd106066eeee267fc77b3161ceb023ab5fddda
features:
- file-system
- network-intensive
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create dpMemIO binPath=C:\\\\windows\\\\temp\\\\dpmemio.sys type=kernel && sc.exe start dpMemIO"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver dpmemio.sys"

# dpmemio.sys

ET&T Technology Co., Ltd. dpmemio.sys (ClevoECView) is a 12KB driver with only 9 imports that provides completely unrestricted arbitrary physical memory read/write and I/O port access with no authentication, no ACL, no address validation, and no size validation. MmUnmapIoSpace is not even imported, meaning every MmMapIoSpace call permanently leaks a system PTE mapping. An additional bug exists where MOVSXD sign-extension on a 32-bit UserBufferPtr provides a write-to-kernel-VA primitive. IOCTLs exposed via \\.\dpMemIO include 0xC80A2420 (arbitrary physical memory READ via MmMapIoSpace), 0xC80A2424 (arbitrary physical memory WRITE via MmMapIoSpace), 0xC80A2410/0xC80A2414 (I/O port read/write byte), 0xC80A2418/0xC80A241C (I/O port read/write variable size), and 0xC80A2428 (version/ping). VeriSign signed with a revoked certificate.

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
