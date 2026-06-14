---
id: windows-credential-dump64
namespace: windows:credential:dump64
name: dump64
description: 'Memory dump tool that comes with Microsoft Visual Studio Located at: C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe.'
author: mr.d0x
version: 1.0.0
capabilities:
- credential.dump
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
- dump64
parameters: []
features: []
execution:
  template: dump64
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Creates a memory dump of the LSASS process. (Create memory dump and parse it offline to retrieve credentials.)
  command: dump64.exe {PID} out.dmp
references:
- label: '1460597833917251595'
  url: https://twitter.com/mrd0x/status/1460597833917251595
techniques:
- credential-access
mitre_ids:
- T1003.001
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dump64.yml
- type: ioc
  description: As a Windows SDK binary, execution on a system may be suspicious
install:
- method: choco
  package_name: dump64
  commands:
  - choco install dump64
---


# dump64

dump64 is a Windows LOLBin. Memory dump tool that comes with Microsoft Visual Studio Located at: C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe.
