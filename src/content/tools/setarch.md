---
id: system-arch-setarch
namespace: system:arch:setarch
name: setarch
description: Set architecture and personality flags, can execute commands.
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
  - linux32
  - linux64
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
  - setarch
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "setarch x86_64 /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via setarch
    command: setarch x86_64 /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/setarch/"
techniques:
  - execution
install:
  - method: apt
    package_name: "util-linux"
    commands:
      - "apt-get install -y util-linux"
---
