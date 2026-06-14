---
id: dev-build-rake
namespace: dev:build:rake
name: rake
description: Ruby build tool, can execute commands via Rakefile.
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
  - make
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
      description: Command execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - rake
  - make
  - Ruby
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "rake /path/to/Rakefile"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via rake
    command: rake /path/to/Rakefile
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rake/"
techniques:
  - execution
install:
  - method: gem
    package_name: "rake"
    commands:
      - "gem install rake"
---
