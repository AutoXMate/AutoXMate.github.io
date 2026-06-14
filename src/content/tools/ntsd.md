---
id: windows-execution-ntsd
namespace: windows:execution:ntsd
name: ntsd
description: 'Symbolic Debugger for Windows. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\ntsd.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\ntsd.exe.'
author: Avihay Eldad
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
- ntsd
parameters: []
features: []
execution:
  template: ntsd
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launches command through the debugging process; optionally add `-G` to exit the debugger automatically. (Executes an executable under a trusted microsoft signed binary.)
  command: ntsd.exe -g {CMD}
references:
- label: cdb-command-line-options
  url: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/cdb-command-line-options
- label: ntsd.exe-629EA12D527237B9CD945AC44C2DE80D.html
  url: https://strontic.github.io/xcyclopedia/library/ntsd.exe-629EA12D527237B9CD945AC44C2DE80D.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections: []
install:
- method: choco
  package_name: ntsd
  commands:
  - choco install ntsd
---


# ntsd

ntsd is a Windows LOLBin. Symbolic Debugger for Windows. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\ntsd.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\ntsd.exe.
