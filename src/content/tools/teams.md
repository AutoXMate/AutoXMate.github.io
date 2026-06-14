---
id: windows-execution-teams
namespace: windows:execution:teams
name: teams
description: 'Electron runtime binary which runs the Teams application Located at: C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe.'
author: Andrew Kisliakov
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
- teams
parameters: []
features: []
execution:
  template: teams
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Generate JavaScript payload and package.json, and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app\\" before executing. (Execute JavaScript code)
  command: teams.exe
- description: Generate JavaScript payload and package.json, archive in ASAR file and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app.asar" before executing. (Execute JavaScript code)
  command: teams.exe
- description: Teams spawns cmd.exe as a child process of teams.exe and executes the ping command (Executes a process under a trusted Microsoft signed binary)
  command: teams.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
references:
- label: ''
  url: https://l--k.uk/2022/01/16/microsoft-teams-and-other-electron-apps-as-lolbins/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.015
detections:
- type: ioc
  description: '%LOCALAPPDATA%\Microsoft\Teams\current\app directory created'
- type: ioc
  description: '%LOCALAPPDATA%\Microsoft\Teams\current\app.asar file created/modified by non-Teams installer/updater'
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/43277f26fc1c81fc98fc79147b711189e901b757/rules/windows/process_creation/proc_creation_win_susp_electron_exeuction_proxy.yml
install:
- method: choco
  package_name: teams
  commands:
  - choco install teams
---


# teams

teams is a Windows LOLBin. Electron runtime binary which runs the Teams application Located at: C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe.
