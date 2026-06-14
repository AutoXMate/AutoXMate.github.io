---
id: windows-execution-setres
namespace: windows:execution:setres
name: setres
description: 'Configures display settings Located at: c:\windows\system32\setres.exe.'
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
- setres
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: setres
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Sets the resolution and then launches 'choice' command from the working
    directory. (Executes arbitrary code)
  command: setres.exe -w 800 -h 600
references:
- label: '1583356502340870144'
  url: https://twitter.com/0gtweet/status/1583356502340870144
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_setres.yml
- type: ioc
  description: Unusual location for choice.exe file
- type: ioc
  description: Process created from choice.com binary
- type: ioc
  description: Existence of choice.cmd file
install:
- method: choco
  package_name: setres
  commands:
  - choco install setres
---

# setres

setres is a Windows LOLBin. Configures display settings Located at: c:\windows\system32\setres.exe.
