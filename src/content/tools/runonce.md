---
id: windows-execution-runonce
namespace: windows:execution:runonce
name: runonce
description: 'Executes a Run Once Task that has been configured in the registry Located
  at: C:\Windows\System32\runonce.exe; C:\Windows\SysWOW64\runonce.exe.'
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
- runonce
parameters: []
features:
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: runonce
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes a Run Once Task that has been configured in the registry.
    (Persistence, bypassing defensive counter measures)
  command: Runonce.exe /AlternateShellStartup
references:
- label: '990717080805789697'
  url: https://twitter.com/pabraeken/status/990717080805789697
- label: ''
  url: https://cmatskas.com/configure-a-runonce-task-on-windows/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_runonce_execution.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/2926e98c5d998706ef7e248a63fb0367c841f685/rules/windows/persistence_run_key_and_startup_broad.toml
- type: ioc
  description: Registy key add - HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\YOURKEY
install:
- method: choco
  package_name: runonce
  commands:
  - choco install runonce
---

# runonce

runonce is a Windows LOLBin. Executes a Run Once Task that has been configured in the registry Located at: C:\Windows\System32\runonce.exe; C:\Windows\SysWOW64\runonce.exe.
