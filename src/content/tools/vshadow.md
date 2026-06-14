---
id: windows-execution-vshadow
namespace: windows:execution:vshadow
name: vshadow
description: 'VShadow is a command-line tool that can be used to create and manage
  volume shadow copies. Located at: C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe.'
author: Ayberk Halaç
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
- vshadow
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: vshadow
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes specified executable from vshadow.exe. (Performs execution
    of specified executable file.)
  command: 'vshadow.exe -nw -exec={PATH_ABSOLUTE:.exe} C:'
references:
- label: vshadow-tool-and-sample
  url: https://learn.microsoft.com/en-us/windows/win32/vss/vshadow-tool-and-sample
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml
- type: ioc
  description: vshadow.exe usage with -exec parameter
install:
- method: choco
  package_name: vshadow
  commands:
  - choco install vshadow
---

# vshadow

vshadow is a Windows LOLBin. VShadow is a command-line tool that can be used to create and manage volume shadow copies. Located at: C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe.
