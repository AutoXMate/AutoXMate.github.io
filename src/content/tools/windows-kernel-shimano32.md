---
id: windows-kernel-shimano32
namespace: windows:kernel:shimano32
name: "shimano32.sys"
description: "HyperTech DNP CrackProof DRM kernel drivers (32-bit and 64-bit variants) from Shimano E-TUBE Project. Expose EPROCESS manipulation IOCTLs (0xAA013880, 0xAA013884, 0xAA013888) similar to capcom.sys exploitation technique. Device accessible at \\\\.\\Htsysm4EFB. Zero detections (0/72 and 0/73) on VirusTotal. Signed by Microsoft WHCP via HyperTech DNP CrackProof (Japanese DRM vendor)."
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
  template: "sc.exe create shimano binPath=C:\\windows\\temp\\shimano64.sys type=kernel && sc.exe start shimano"
  sandbox: execFile
  timeout_seconds: 30
  shell: true
install:
  - method: custom
    description: "Load shimano32.sys kernel driver"
    commands:
      - "sc.exe create shimano binPath=C:\\windows\\temp\\shimano64.sys type=kernel && sc.exe start shimano"
references:
  - label: "Reference"
    url: "https://github.com/magicsword-io/LOLDrivers/issues/163"
---
examples:
  - description: "Load the kernel driver"
    command: "sc.exe create shimano binPath=C:\\\\windows\\\\temp\\\\shimano64.sys type=kernel && sc.exe start shimano"
  - description: "Exploit the driver for privilege escalation"
    command: "Exploit.exe --driver shimano32.sys"

# shimano32.sys

HyperTech DNP CrackProof DRM kernel drivers (32-bit and 64-bit variants) from Shimano E-TUBE Project. Expose EPROCESS manipulation IOCTLs (0xAA013880, 0xAA013884, 0xAA013888) similar to capcom.sys exploitation technique. Device accessible at \\.\Htsysm4EFB. Zero detections (0/72 and 0/73) on VirusTotal. Signed by Microsoft WHCP via HyperTech DNP CrackProof (Japanese DRM vendor).

**Use Case:** Elevate privileges

**Required Privileges:** kernel

**MITRE ATT&CK:** T1068