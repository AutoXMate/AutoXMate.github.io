---
id: windows-kernel-devhost
namespace: windows:kernel:devhost
name: devhost.sys
description: devhost.sys is a WHQL attestation-signed kernel driver that exposes arbitrary
  memory read primitives to usermode. The device object at \\.\devhost has no ACL
  beyond a device handle. At load, the driver reads IA32_LSTAR MSR to locate ntoskrnl
  base via backward MZ walk, then dynamically resolves APIs (including MmMapIoSpace
  and MmCopyMemory) using a djb2-style hash algorithm over the PE export directory.
  Only 11 benign imports are visible statically. The system CR3 is leaked to user-mode
  at Dri...
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
  template: sc.exe create devhost binPath=C:\windows\temp\devhost.sys type=kernel
    && sc.exe start devhost
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
- method: custom
  description: Load devhost.sys kernel driver
  commands:
  - sc.exe create devhost binPath=C:\windows\temp\devhost.sys type=kernel && sc.exe
    start devhost
references:
- label: Reference
  url: https://x.com/nextaboratory/status/1914729845602783262
features:
- compression
- file-system
- pipes-stdout
- requires-root
---

examples:
  - description: "Load the kernel driver"
    command: "sc.exe create devhost binPath=C:\\\\windows\\\\temp\\\\devhost.sys type=kernel && sc.exe start devhost"

# devhost.sys

devhost.sys is a WHQL attestation-signed kernel driver that exposes arbitrary memory read primitives to usermode. The device object at \\.\devhost has no ACL beyond a device handle. At load, the driver reads IA32_LSTAR MSR to locate ntoskrnl base via backward MZ walk, then dynamically resolves APIs (including MmMapIoSpace and MmCopyMemory) using a djb2-style hash algorithm over the PE export directory. Only 11 benign imports are visible statically. The system CR3 is leaked to user-mode at DriverEntry. Authentication uses a hardcoded magic cookie via IOCTL 0x28E017. IOCTL 0x28E01B accepts a caller-supplied CR3 and target virtual address, performs a manual 4-level x64 page-table walk (PML4-PDPT-PD-PT), and reads physical memory via MmMapIoSpace. Additional IOCTLs expose NtBuildNumber, PsLoadedModuleList, and per-CPU KPCR CurrentThread. Nextron Research noted that these primitives are tailor-made for credential theft (e.g. LSASS memory dumping), though no confirmed malicious usage has been publicly documented. WHQL attestation signed with active cert (Nov 2025-Nov 2026). SpcSpOpusInfo identifies the submitter as Shenzhen Aolian Information Security Technology Co Ltd.

**Use Case:** Arbitrary kernel memory read via page-table walk and MmMapIoSpace

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068
