---
id: windows-execution-stordiag
namespace: windows:execution:stordiag
name: stordiag
description: 'Storage diagnostic tool Located at: c:\windows\system32\stordiag.exe; c:\windows\syswow64\stordiag.exe.'
author: Eral4m
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
risk_level: high
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
- stordiag
parameters: []
features: []
execution:
  template: stordiag
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, Stordiag.exe will execute schtasks.exe systeminfo.exe and fltmc.exe - if stordiag.exe is copied to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it. (Possible defence evasion purposes.)
  command: stordiag.exe
- description: Once executed, Stordiag.exe will execute schtasks.exe and powershell.exe - if stordiag.exe is copied to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it. (Possible defence evasion purposes.)
  command: stordiag.exe
references:
- label: '1451112385041911809'
  url: https://twitter.com/eral4m/status/1451112385041911809
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml
- type: ioc
  description: systeminfo.exe, fltmc.exe or schtasks.exe or powershell.exe being executed outside of their normal path of c:\windows\system32\ or c:\windows\syswow64\
install:
- method: choco
  package_name: stordiag
  commands:
  - choco install stordiag
---


# stordiag

stordiag is a Windows LOLBin. Storage diagnostic tool Located at: c:\windows\system32\stordiag.exe; c:\windows\syswow64\stordiag.exe.
