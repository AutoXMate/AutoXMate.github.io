---
id: network-diagnostic-fping
namespace: network:diagnostic:fping
name: fping
description: Fast ping tool, can execute commands via crafted packets.
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
  - ping
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - fping
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "fping -e /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via fping
    command: fping -e /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/fping/"
techniques:
  - execution
install:
  - method: apt
    package_name: "fping"
    commands:
      - "apt-get install -y fping"
---
