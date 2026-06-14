---
id: dev-npm-npm
namespace: dev:npm:npm
name: npm
description: Node package manager, can execute commands via pre/postinstall scripts.
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
  - node
  - yarn
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
    - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
  - npm
  - node
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "npm -C /path/to/dir run build"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via npm script
    command: |
      echo '{"scripts":{"x":"/bin/sh"}}' >package.json
      npm -C . run x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/npm/"
techniques:
  - execution
install:
  - method: npm
    package_name: "npm"
    commands:
      - "npm install -g npm"
---
