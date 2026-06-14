---
id: system-terminal-openvt
namespace: system:terminal:openvt
name: openvt
description: Run a program on a new VT, can execute commands.
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
related_tools:
  - chvt
  - deallocvt
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
  - openvt
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "openvt /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via openvt
    command: openvt /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/openvt/"
techniques:
  - execution
install:
  - method: apt
    package_name: "kbd"
    commands:
      - "apt-get install -y kbd"
---
