---
id: process-lock-setlock
namespace: process:lock:setlock
name: setlock
description: Lock file and execute command, can execute commands.
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
  - flock
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
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - setlock
  - flock
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "setlock /path/to/lock /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via setlock
    command: setlock /path/to/lock /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/setlock/"
techniques:
  - execution
install:
  - method: apt
    package_name: "daemontools"
    commands:
      - "apt-get install -y daemontools"
---
