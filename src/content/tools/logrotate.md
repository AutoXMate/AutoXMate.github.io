---
id: system-log-rotate
namespace: system:log:rotate
name: logrotate
description: Log rotation utility, can execute commands via crafted config files.
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
  - logrotate
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "logrotate -f /path/to/config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via logrotate
    command: logrotate -f /path/to/config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/logrotate/"
techniques:
  - execution
install:
  - method: apt
    package_name: "logrotate"
    commands:
      - "apt-get install -y logrotate"
---
