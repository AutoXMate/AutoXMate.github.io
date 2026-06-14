---
id: windows-execution-pnputil
namespace: windows:execution:pnputil
name: pnputil
description: 'Used for installing drivers Located at: C:\Windows\system32\pnputil.exe.'
author: Hai vaknin (lux)
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
- pnputil
parameters: []
features: []
execution:
  template: pnputil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Used for installing drivers (Add malicious driver)
  command: pnputil.exe -i -a {PATH_ABSOLUTE:.inf}
references: []
techniques:
- execution
- persistence
mitre_ids:
- T1547
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml
install:
- method: choco
  package_name: pnputil
  commands:
  - choco install pnputil
---


# pnputil

pnputil is a Windows LOLBin. Used for installing drivers Located at: C:\Windows\system32\pnputil.exe.
