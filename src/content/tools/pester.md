---
id: windows-execution-pester
namespace: windows:execution:pester
name: pester
description: 'Used as part of the Powershell pester Located at: c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat.'
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
- pester
parameters: []
features: []
execution:
  template: pester
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute code using Pester. The third parameter can be anything. The fourth is the payload. (Proxy execution)
  command: Pester.bat [/help|?|-?|/?] "$null; {CMD}"
- description: Execute code using Pester. Example here executes specified executable. (Proxy execution)
  command: Pester.bat ;{PATH:.exe}
references:
- label: '993383596244258816'
  url: https://twitter.com/Oddvarmoe/status/993383596244258816
- label: '1560072680887525378'
  url: https://twitter.com/_st0pp3r_/status/1560072680887525378
- label: '1560072680887525378'
  url: https://twitter.com/_st0pp3r_/status/1560072680887525378
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml
install:
- method: choco
  package_name: pester
  commands:
  - choco install pester
---


# pester

pester is a Windows LOLBin. Used as part of the Powershell pester Located at: c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat.
