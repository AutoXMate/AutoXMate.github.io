---
id: config-puppet-puppet
namespace: config:puppet:puppet
name: puppet
description: Configuration management tool, can execute Ruby code.
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
  - facter
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
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - puppet
  - facter
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "puppet apply -e 'exec { \"/bin/sh\": }'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via puppet
    command: "puppet apply -e 'exec { \"/bin/sh\": }'"
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/puppet/"
techniques:
  - execution
install:
  - method: apt
    package_name: "puppet"
    commands:
      - "apt-get install -y puppet"
---
