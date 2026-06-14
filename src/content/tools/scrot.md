---
id: image-capture-scrot
namespace: image:capture:scrot
name: scrot
description: Screenshot tool, can execute commands via exec/postexec options.
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
related_tools:
  - import
  - maim
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
  - scrot
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "scrot -e '/bin/sh'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via scrot
    command: scrot -e '/bin/sh'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/scrot/"
techniques:
  - execution
install:
  - method: apt
    package_name: "scrot"
    commands:
      - "apt-get install -y scrot"
---
