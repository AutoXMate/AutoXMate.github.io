---
id: windows-uacbypass-iscsicpl
namespace: windows:uacbypass:iscsicpl
name: iscsicpl
description: 'Microsoft iSCSI Initiator Control Panel tool Located at: c:\windows\system32\iscsicpl.exe; c:\windows\syswow64\iscsicpl.exe.'
author: Ekitji
version: 1.0.0
capabilities:
- security.privilege-escalation.uac-bypass
platforms:
- windows
risk_level: critical
trust_level: community
execution_policy: enabled
architectures:
- amd64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - privilege_escalation
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- iscsicpl
parameters: []
features: []
execution:
  template: iscsicpl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: c:\windows\syswow64\iscsicpl.exe has a DLL injection through `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll`, resulting in UAC bypass. (Execute a custom DLL via a trusted high-integrity process without a UAC prompt.)
  command: c:\windows\syswow64\iscsicpl.exe
- description: Both `c:\windows\system32\iscsicpl.exe` and `c:\windows\system64\iscsicpl.exe` have UAC bypass through launching iscicpl.exe, then navigating into the Configuration tab, clicking Report, then launching your custom command. (Execute a binary or script as a high-integrity process without a UAC prompt.)
  command: iscsicpl.exe
references:
- label: iscsi-initiator-portal
  url: https://learn.microsoft.com/en-us/windows-server/storage/iscsi/iscsi-initiator-portal
- label: iscsicpl_bypassUAC
  url: https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC
techniques:
- privilege-escalation
mitre_ids:
- T1548.002
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml
- type: ioc
  description: C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll
- type: ioc
  description: Suspicious child process to iscsicpl.exe like cmd, powershell etc.
install:
- method: choco
  package_name: iscsicpl
  commands:
  - choco install iscsicpl
---


# iscsicpl

iscsicpl is a Windows LOLBin. Microsoft iSCSI Initiator Control Panel tool Located at: c:\windows\system32\iscsicpl.exe; c:\windows\syswow64\iscsicpl.exe.
