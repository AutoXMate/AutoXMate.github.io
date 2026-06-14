---
id: windows-execution-reset
namespace: windows:execution:reset
name: reset
description: 'Remote Desktop Services Reset Utility Located at: c:\windows\system32\reset.exe;
  c:\windows\syswow64\reset.exe.'
author: Matan Bahar
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
- reset
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
- remote
execution:
  template: reset
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, `reset.exe` will execute `rwinsta.exe` in the same folder.
    Thus, if `reset.exe` is copied to a folder and an arbitrary executable is renamed
    to `rwinsta.exe`, `reset.exe` will spawn it. (Execute an arbitrary executable
    via trusted system executable.)
  command: reset.exe session
references: []
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: ioc
  description: reset.exe being executed and executes rwinsta.exe outside of its normal
    path of c:\windows\system32\ or c:\windows\syswow64\
install:
- method: choco
  package_name: reset
  commands:
  - choco install reset
---

# reset

reset is a Windows LOLBin. Remote Desktop Services Reset Utility Located at: c:\windows\system32\reset.exe; c:\windows\syswow64\reset.exe.
