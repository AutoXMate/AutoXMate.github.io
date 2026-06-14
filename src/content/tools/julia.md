---
id: math-julia-julia
namespace: math:julia:julia
name: julia
description: Julia language REPL, can execute commands and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 64
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 64
  network: none
  disk_io: low
allowed-tools:
  - julia
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "julia -e 'run(`/bin/sh`)'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via julia
    command: julia -e 'run(`/bin/sh`)'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/julia/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "julia"
    commands:
      - "apt-get install -y julia"
---
