---
id: windows-execution-logger
namespace: windows:execution:logger
name: logger
description: 'A logging configuration tool from the Windows Kits used to start and manage process logging. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\logger.exe; C:\Program Files\Windows Kits\10\Debuggers\x86\logger.exe.'
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
- logger
parameters: []
features: []
execution:
  template: logger
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes the command specified after the `RUN` parameter as a child of `logger.exe`. (Executes an abitrary command via a signed binary to evade detection.)
  command: logger.exe RUN "{CMD}"
- description: Executes the command specified after the `RUNW` parameter as a child of `logger.exe`. (Executes an abitrary command via a signed binary to evade detection.)
  command: logger.exe RUNW "{CMD}"
- description: Executes the command specified as a child of `logger.exe`. (Executes an abitrary command via a signed binary to evade detection.)
  command: logger.exe "{CMD}"
references:
- label: logger
  url: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/logger
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections: []
install:
- method: choco
  package_name: logger
  commands:
  - choco install logger
---


# logger

logger is a Windows LOLBin. A logging configuration tool from the Windows Kits used to start and manage process logging. Located at: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe; C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\logger.exe; C:\Program Files\Windows Kits\10\Debuggers\x86\logger.exe.
