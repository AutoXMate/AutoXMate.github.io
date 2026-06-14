---
id: windows-execution-query
namespace: windows:execution:query
name: query
description: 'Remote Desktop Services MultiUser Query Utility Located at: c:\windows\system32\query.exe; c:\windows\syswow64\query.exe.'
author: Idan Lerman
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
- query
parameters: []
features: []
execution:
  template: query
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, `query.exe` will execute `quser.exe` in the same folder. Thus, if `query.exe` is copied to a folder and an arbitrary executable is renamed to `quser.exe`, `query.exe` will spawn it. Instead of `user`, it is also possible to use `session`, `termsession` or `process` as command-line option. (Execute an arbitrary executable via trusted system executable.)
  command: query.exe user
references: []
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: ioc
  description: query.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
install:
- method: choco
  package_name: query
  commands:
  - choco install query
---


# query

query is a Windows LOLBin. Remote Desktop Services MultiUser Query Utility Located at: c:\windows\system32\query.exe; c:\windows\syswow64\query.exe.
