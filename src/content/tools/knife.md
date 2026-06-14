---
id: config-chef-knife
namespace: config:chef:knife
name: knife
description: Chef CLI, can execute Ruby code.
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
  - chef
  - ruby
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
      description: Ruby code execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - knife
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "knife exec -E 'exec \"/bin/sh\"'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via knife
    command: knife exec -E 'exec "/bin/sh"'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/knife/"
techniques:
  - execution
install:
  - method: gem
    package_name: "knife"
    commands:
      - "gem install knife"
---
