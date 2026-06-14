---
id: system-terminal-mosh
namespace: system:terminal:mosh
name: mosh-server
description: Mobile shell server, can execute commands.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- linux
- macos
- bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- ssh
artifacts: []
workflow_edges:
  produces:
  - command-execution
  consumes:
  - execution-context
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
- mosh-server
- Bash
- execFile
parameters: []
features:
- process-manip
execution:
  template: mosh-server /path/to/command
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute command via mosh-server
  command: mosh-server /path/to/command
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/mosh-server/
techniques:
- execution
install:
- method: apt
  package_name: mosh
  commands:
  - apt-get install -y mosh
mitre_ids:
- T1059
---


