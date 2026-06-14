---
id: windows-execution-wt
namespace: windows:execution:wt
name: wt
description: 'Windows Terminal Located at: C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe.'
author: Nasreddine Bencherchali
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
- wt
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: wt
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute a command via Windows Terminal. (Use wt.exe as a proxy binary
    to evade defensive counter-measures)
  command: wt.exe {CMD}
references:
- label: '1552100271668469761'
  url: https://twitter.com/nas_bench/status/1552100271668469761
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml
install:
- method: choco
  package_name: wt
  commands:
  - choco install wt
---

# wt

wt is a Windows LOLBin. Windows Terminal Located at: C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe.
