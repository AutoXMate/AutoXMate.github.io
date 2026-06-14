---
id: text-display-cowthink
namespace: text:display:cowthink
name: cowthink
description: Configurable thinking cow, can execute Perl code inherited from Perl binary.
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
  - cowsay
  - perl
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
      description: Perl code execution output
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
  - cowthink
  - cowsay
  - perl
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "cowthink -f {script} x"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Perl code via cowthink
    command: cowthink -f /path/to/script.pl x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cowthink/"
techniques:
  - execution
install:
  - method: apt
    package_name: "cowsay"
    commands:
      - "apt-get install -y cowsay"
---
