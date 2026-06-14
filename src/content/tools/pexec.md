---
id: process-exec-pexec
namespace: process:exec:pexec
name: pexec
description: Execute command in parallel, can execute commands.
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
  - xargs
  - parallel
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
  - pexec
  - xargs
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "pexec /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via pexec
    command: pexec /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pexec/"
techniques:
  - execution
install:
  - method: apt
    package_name: "pexec"
    commands:
      - "apt-get install -y pexec"
---
