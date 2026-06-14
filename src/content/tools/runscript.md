---
id: process-runscript
namespace: process:control:runscript
name: runscript
description: Run script command, can execute commands.
author: "GTFOBins"
version: "1.0.0"
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
related_tools: []
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
  - runscript
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "runscript /path/to/script"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via runscript
    command: runscript /path/to/script
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/runscript/"
techniques:
  - execution
install:
  - method: apt
    package_name: "runscript"
    commands:
      - "apt-get install -y runscript"
---
