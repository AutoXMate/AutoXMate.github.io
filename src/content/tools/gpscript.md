---
id: windows-execution-gpscript
namespace: windows:execution:gpscript
name: gpscript
description: 'Used by group policy to process scripts Located at: C:\Windows\System32\gpscript.exe; C:\Windows\SysWOW64\gpscript.exe.'
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
- gpscript
parameters: []
features: []
execution:
  template: gpscript
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes logon scripts configured in Group Policy. (Add local group policy logon script to execute file and hide from defensive counter measures)
  command: Gpscript /logon
- description: Executes startup scripts configured in Group Policy (Add local group policy logon script to execute file and hide from defensive counter measures)
  command: Gpscript /startup
references:
- label: ''
  url: https://oddvar.moe/2018/04/27/gpscript-exe-another-lolbin-to-the-list/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_gpscript.yml
- type: ioc
  description: Scripts added in local group policy
- type: ioc
  description: Execution of Gpscript.exe after logon
install:
- method: choco
  package_name: gpscript
  commands:
  - choco install gpscript
---


# gpscript

gpscript is a Windows LOLBin. Used by group policy to process scripts Located at: C:\Windows\System32\gpscript.exe; C:\Windows\SysWOW64\gpscript.exe.
