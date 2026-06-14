---
id: windows-execution-utilityfunctions
namespace: windows:execution:utilityfunctions
name: utilityfunctions
description: 'PowerShell Diagnostic Script Located at: C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1.'
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
- utilityfunctions
parameters: []
features:
- interactive
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: utilityfunctions
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Proxy execute Managed DLL with PowerShell (Execute proxied payload
    with Microsoft signed binary)
  command: powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking;
    import-module .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[Program.Class]::Main()"
references:
- label: '1441003666274668546'
  url: https://twitter.com/nickvangilder/status/1441003666274668546
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/0.21-688-gd172b136b/rules/windows/process_creation/proc_creation_win_lolbas_utilityfunctions.yml
install:
- method: choco
  package_name: utilityfunctions
  commands:
  - choco install utilityfunctions
---

# utilityfunctions

utilityfunctions is a Windows LOLBin. PowerShell Diagnostic Script Located at: C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1.
