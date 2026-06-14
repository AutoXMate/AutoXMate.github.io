---
id: math-r-lang
namespace: math:r:lang
name: R
description: R language for statistics, can execute commands.
author: "GTFOBins"
version: "1.0.0"
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
  - octave
  - julia
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
      description: R script output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - R
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "R -e 'system(\"/bin/sh\")'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via R
    command: R -e 'system("/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/R/"
techniques:
  - execution
install:
  - method: apt
    package_name: "r-base"
    commands:
      - "apt-get install -y r-base"
---
