---
id: dev-ruby-byebug
namespace: dev:ruby:byebug
name: byebug
description: Ruby debugger, can execute Ruby code inherited from Ruby binary.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - macos
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - ruby
artifacts: []
workflow_edges:
  produces:
    - command-execution
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or unprivileged execution context
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
  - byebug
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "byebug --no-stop /path/to/script.rb"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Ruby code via byebug
    command: byebug --no-stop /path/to/script.rb
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/byebug/"
techniques:
  - execution
install:
  - method: gem
    package_name: "byebug"
    commands:
      - "gem install byebug"
---
