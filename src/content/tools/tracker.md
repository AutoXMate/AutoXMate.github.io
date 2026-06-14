---
id: windows-execution-tracker
namespace: windows:execution:tracker
name: tracker
description: 'Tool included with Microsoft .Net Framework. Located at: no default.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- security.defense-evasion.bypass
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
- tracker
parameters: []
features:
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: tracker
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use tracker.exe to proxy execution of an arbitrary DLL into another
    process. Since tracker.exe is also signed it can be used to bypass application
    whitelisting solutions. (Injection of locally stored DLL file into target process.)
  command: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
- description: Use tracker.exe to proxy execution of an arbitrary DLL into another
    process. Since tracker.exe is also signed it can be used to bypass application
    whitelisting solutions. (Injection of locally stored DLL file into target process.)
  command: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
references:
- label: '793151392185589760'
  url: https://twitter.com/subTee/status/793151392185589760
- label: Execution
  url: https://attack.mitre.org/wiki/Execution
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml
install:
- method: choco
  package_name: tracker
  commands:
  - choco install tracker
---

# tracker

tracker is a Windows LOLBin. Tool included with Microsoft .Net Framework. Located at: no default.
