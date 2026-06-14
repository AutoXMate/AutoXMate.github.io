---
id: system-info-facter
namespace: system:info:facter
name: facter
description: System inventory and configuration tool, can execute Ruby code via custom facts.
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
  - puppet
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
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - facter
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "facter -p custom/fact.rb"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Ruby code via facter custom fact
    command: |
      mkdir -p /tmp/custom_facts
      echo "Facter.add('x') { setcode { system('/bin/sh') } }" >/tmp/custom_facts/x.rb
      facter -p custom_facts=/tmp/custom_facts x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/facter/"
techniques:
  - execution
install:
  - method: gem
    package_name: "facter"
    commands:
      - "gem install facter"
---
