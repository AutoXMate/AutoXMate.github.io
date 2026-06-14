---
id: math-plot-gnuplot
namespace: math:plot:gnuplot
name: gnuplot
description: Plotting utility, can execute commands.
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
  - gnuplot
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: 'gnuplot -e "system(\"/bin/sh\")"'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via gnuplot
    command: gnuplot -e 'system("/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/gnuplot/"
techniques:
  - execution
install:
  - method: apt
    package_name: "gnuplot"
    commands:
      - "apt-get install -y gnuplot"
---
