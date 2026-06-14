---
id: windows-execution-te
namespace: windows:execution:te
name: te
description: 'Testing tool included with Microsoft Test Authoring and Execution Framework
  (TAEF). Located at: no default.'
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
- te
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: te
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Run COM Scriptlets (e.g. VBScript) by calling a Windows Script Component
    (WSC) file. (Execute Visual Basic script stored in local Windows Script Component
    file.)
  command: te.exe {PATH:.wsc}
- description: Execute commands from a DLL file with Test Authoring and Execution
    Framework (TAEF) tests. See resources section for required structures. (Execute
    DLL file.)
  command: te.exe {PATH:.dll}
references:
- label: '927680266390384640'
  url: https://twitter.com/gn3mes1s/status/927680266390384640
- label: '359'
  url: https://github.com/LOLBAS-Project/LOLBAS/pull/359
- label: authoring-tests
  url: https://learn.microsoft.com/en-us/windows-hardware/drivers/taef/authoring-tests
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml
install:
- method: choco
  package_name: te
  commands:
  - choco install te
---

# te

te is a Windows LOLBin. Testing tool included with Microsoft Test Authoring and Execution Framework (TAEF). Located at: no default.
