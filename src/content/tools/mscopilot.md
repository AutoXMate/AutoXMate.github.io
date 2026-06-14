---
id: windows-execution-mscopilot
namespace: windows:execution:mscopilot
name: mscopilot
description: 'Microsoft Copilot app Located at: C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot.exe.'
author: 4n4s4zi
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
- mscopilot
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: mscopilot
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: '`mscopilot.exe` will spawn the provided command. Parent `mscopilot.exe`
    process needs to be killed to avoid command being executed an infinite number
    of times. (Executes a process under a trusted Microsoft signed binary)'
  command: mscopilot.exe --no-startup-window --disable-gpu-sandbox --gpu-launcher="{CMD}
    && taskkill /f /im mscopilot.exe &&"
references:
- label: tour-de-mscopilot
  url: https://github.com/4n4s4zi/tour-de-mscopilot
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.015
detections: []
install:
- method: choco
  package_name: mscopilot
  commands:
  - choco install mscopilot
---

# mscopilot

mscopilot is a Windows LOLBin. Microsoft Copilot app Located at: C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot.exe.
