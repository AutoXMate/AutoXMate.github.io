---
id: windows-execution-write
namespace: windows:execution:write
name: write
description: 'Windows Write Located at: C:\Windows\write.exe; C:\Windows\System32\write.exe;
  C:\Windows\SysWOW64\write.exe.'
author: Michal Belzak
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
- write
parameters: []
features:
- file-system
- pipes-stdin
- pipes-stdout
execution:
  template: write
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes a binary provided in default value of `HKCU\Software\Microsoft\Windows\CurrentVersion\App
    Paths\wordpad.exe`. (Execute binary through legitimate proxy. This might be utilized
    to confuse detection solutions that rely on parent-child relationships.)
  command: write.exe
references:
- label: b8c5ff7c2bd0fb2b385cc2fdd119874b
  url: https://gist.github.com/mblzk/b8c5ff7c2bd0fb2b385cc2fdd119874b
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: ioc
  description: Changes to HKCU:\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml
install:
- method: choco
  package_name: write
  commands:
  - choco install write
---

# write

write is a Windows LOLBin. Windows Write Located at: C:\Windows\write.exe; C:\Windows\System32\write.exe; C:\Windows\SysWOW64\write.exe.
