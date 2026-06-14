---
id: windows-execution-vsls-agent
namespace: windows:execution:vsls-agent
name: vsls-agent
description: 'Agent for Visual Studio Live Share (Code Collaboration) Located at:
  c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe.'
author: Jimmy (@bohops)
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
- vsls-agent
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: vsls-agent
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Load a library payload using the --agentExtensionPath parameter (32-bit)
    (Execute proxied payload with Microsoft signed binary)
  command: vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll}
references:
- label: '1583916360404729857'
  url: https://twitter.com/bohops/status/1583916360404729857
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml
install:
- method: choco
  package_name: vsls-agent
  commands:
  - choco install vsls-agent
---

# vsls-agent

vsls-agent is a Windows LOLBin. Agent for Visual Studio Live Share (Code Collaboration) Located at: c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe.
