---
id: windows-execution-windbg
namespace: windows:execution:windbg
name: windbg
description: 'Windows Debugger for advanced user-mode and kernel-mode debugging. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\windbg.exe.'
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
- windbg
parameters: []
features: []
execution:
  template: windbg
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launches a command line through the debugging process; optionally add `-G` to exit the debugger automatically. (Executes an executable under a trusted microsoft signed binary.)
  command: windbg.exe -g {CMD}
references:
- label: windbg-command-line-options
  url: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/windbg-command-line-options
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections: []
install:
- method: choco
  package_name: windbg
  commands:
  - choco install windbg
---


# windbg

windbg is a Windows LOLBin. Windows Debugger for advanced user-mode and kernel-mode debugging. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\windbg.exe.
