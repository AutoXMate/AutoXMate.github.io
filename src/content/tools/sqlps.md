---
id: windows-execution-sqlps
namespace: windows:execution:sqlps
name: sqlps
description: Tool included with Microsoft SQL Server that loads SQL Server cmdlets.
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
- sqlps
parameters: []
features: []
execution:
  template: sqlps
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples: []
references: []
techniques:
- execution
mitre_ids: []
detections: []
install:
- method: choco
  package_name: sqlps
  commands:
  - choco install sqlps
---


# sqlps

sqlps is a Windows LOLBin.
