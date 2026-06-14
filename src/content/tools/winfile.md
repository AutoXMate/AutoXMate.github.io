---
id: windows-execution-winfile
namespace: windows:execution:winfile
name: winfile
description: 'Windows File Manager executable Located at: C:\Windows\System32\winfile.exe; C:\Windows\winfile.exe; C:\Program Files\WinFile\winfile.exe.'
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
- winfile
parameters: []
features: []
execution:
  template: winfile
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute an executable file with WinFile as a parent process. (Performs execution of specified file, can be used as a defense evasion)
  command: winfile.exe {PATH:.exe}
references:
- label: winfile
  url: https://github.com/microsoft/winfile
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections: []
install:
- method: choco
  package_name: winfile
  commands:
  - choco install winfile
---


# winfile

winfile is a Windows LOLBin. Windows File Manager executable Located at: C:\Windows\System32\winfile.exe; C:\Windows\winfile.exe; C:\Program Files\WinFile\winfile.exe.
