---
id: system-terminal-rlwrap
namespace: system:terminal:rlwrap
name: rlwrap
description: Readline wrapper, can execute commands.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- linux
- bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- rlfe
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
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
- rlwrap
- Bash
- execFile
parameters: []
features:
- process-manip
execution:
  template: rlwrap /path/to/command
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute command via rlwrap
  command: rlwrap /path/to/command
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/rlwrap/
techniques:
- execution
install:
- method: apt
  package_name: rlwrap
  commands:
  - apt-get install -y rlwrap
mitre_ids:
- T1059
---


