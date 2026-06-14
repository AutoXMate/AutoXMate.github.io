---
id: windows-execution-cl-loadassembly
namespace: windows:execution:cl-loadassembly
name: cl-loadassembly
description: 'PowerShell Diagnostic Script Located at: C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1.'
author: Jimmy (@bohops)
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
- cl-loadassembly
parameters: []
features: []
execution:
  template: cl-loadassembly
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Proxy execute Managed DLL with PowerShell (Execute proxied payload with Microsoft signed binary)
  command: powershell.exe -ep bypass -command "set-location -path C:\Windows\diagnostics\system\Audio; import-module .\CL_LoadAssembly.ps1; LoadAssemblyFromPath ..\..\..\..\testing\fun.dll;[Program]::Fun()"
references:
- label: ''
  url: https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-powershell-diagnostic-scripts/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/ff6c54ded6b52f379cec11fe17c1ccb956faa660/rules/windows/process_creation/proc_creation_win_lolbas_cl_loadassembly.yml
install:
- method: choco
  package_name: cl-loadassembly
  commands:
  - choco install cl-loadassembly
---


# cl-loadassembly

cl-loadassembly is a Windows LOLBin. PowerShell Diagnostic Script Located at: C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1.
