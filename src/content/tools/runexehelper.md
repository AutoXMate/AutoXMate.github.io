---
id: windows-execution-runexehelper
namespace: windows:execution:runexehelper
name: runexehelper
description: 'Launcher process Located at: c:\windows\system32\runexehelper.exe.'
author: Grzegorz Tworek
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
- runexehelper
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: runexehelper
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: 'Launches the specified exe. Prerequisites: (1) diagtrack_action_output
    environment variable must be set to an existing, writable folder; (2) runexewithargs_output.txt
    file cannot exist in the folder indicated by the variable. (Executes arbitrary
    code)'
  command: runexehelper.exe {PATH_ABSOLUTE:.exe}
references:
- label: '1206692239839289344'
  url: https://twitter.com/0gtweet/status/1206692239839289344
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml
- type: ioc
  description: c:\windows\system32\runexehelper.exe is run
- type: ioc
  description: Existence of runexewithargs_output.txt file
install:
- method: choco
  package_name: runexehelper
  commands:
  - choco install runexehelper
---

# runexehelper

runexehelper is a Windows LOLBin. Launcher process Located at: c:\windows\system32\runexehelper.exe.
