---
id: windows-execution-workfolders
namespace: windows:execution:workfolders
name: workfolders
description: 'Work Folders Located at: C:\Windows\System32\WorkFolders.exe.'
author: Elliot Killick
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
- workfolders
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: workfolders
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute `control.exe` in the current working directory (Can be used
    to evade defensive countermeasures or to hide as a persistence mechanism)
  command: WorkFolders
- description: '`WorkFolders` attempts to execute `control.exe`. By modifying the
    default value of the App Paths registry key for `control.exe` in `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\App
    Paths\control.exe`, an attacker can achieve proxy execution. (Proxy execution
    of a malicious payload via App Paths registry hijacking.)'
  command: WorkFolders
references:
- label: ''
  url: https://www.ctus.io/2021/04/12/exploading/
- label: '1449812843772227588'
  url: https://twitter.com/ElliotKillick/status/1449812843772227588
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_workfolders.yml
- type: ioc
  description: WorkFolders.exe should not be run on a normal workstation
- type: ioc
  description: Registry modification to HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\App
    Paths\control.exe
install:
- method: choco
  package_name: workfolders
  commands:
  - choco install workfolders
---

# workfolders

workfolders is a Windows LOLBin. Work Folders Located at: C:\Windows\System32\WorkFolders.exe.
