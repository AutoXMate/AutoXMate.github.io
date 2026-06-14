---
id: windows-execution-vsjitdebugger
namespace: windows:execution:vsjitdebugger
name: vsjitdebugger
description: 'Just-In-Time (JIT) debugger included with Visual Studio Located at:
  c:\windows\system32\vsjitdebugger.exe.'
author: Oddvar Moe
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
- vsjitdebugger
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: vsjitdebugger
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes specified executable as a subprocess of Vsjitdebugger.exe.
    (Execution of local PE file as a subprocess of Vsjitdebugger.exe.)
  command: Vsjitdebugger.exe {PATH:.exe}
references:
- label: '990758590020452353'
  url: https://twitter.com/pabraeken/status/990758590020452353
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml
install:
- method: choco
  package_name: vsjitdebugger
  commands:
  - choco install vsjitdebugger
---

# vsjitdebugger

vsjitdebugger is a Windows LOLBin. Just-In-Time (JIT) debugger included with Visual Studio Located at: c:\windows\system32\vsjitdebugger.exe.
