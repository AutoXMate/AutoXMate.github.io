---
id: windows-execution-wuauclt
namespace: windows:execution:wuauclt
name: wuauclt
description: 'Windows Update Client Located at: C:\Windows\System32\wuauclt.exe; C:\Windows\UUS\amd64\wuauclt.exe.'
author: David Middlehurst
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
- wuauclt
parameters: []
features: []
execution:
  template: wuauclt
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Loads and executes DLL code on attach. (Execute dll via attach/detach methods)
  command: wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer
references:
- label: ''
  url: https://dtm.uk/wuauclt/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wuauclt.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wuauclt_execution.yml
- type: ioc
  description: wuauclt run with a parameter of a DLL path
- type: ioc
  description: Suspicious wuauclt Internet/network connections
install:
- method: choco
  package_name: wuauclt
  commands:
  - choco install wuauclt
---


# wuauclt

wuauclt is a Windows LOLBin. Windows Update Client Located at: C:\Windows\System32\wuauclt.exe; C:\Windows\UUS\amd64\wuauclt.exe.
