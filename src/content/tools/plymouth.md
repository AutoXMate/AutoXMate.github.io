---
id: boot-plymouth-plymouth
namespace: boot:plymouth:plymouth
name: plymouth
description: Boot screen daemon, can execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - plymouth
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "plymouth /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via plymouth
    command: plymouth /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/plymouth/"
techniques:
  - execution
install:
  - method: apt
    package_name: "plymouth"
    commands:
      - "apt-get install -y plymouth"
---
