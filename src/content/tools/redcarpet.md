---
id: text-process-redcarpet
namespace: text:process:redcarpet
name: redcarpet
description: Markdown renderer, can execute commands.
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
  - redcarpet
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "redcarpet /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via redcarpet
    command: redcarpet /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/redcarpet/"
techniques:
  - execution
install:
  - method: gem
    package_name: "redcarpet"
    commands:
      - "gem install redcarpet"
---
