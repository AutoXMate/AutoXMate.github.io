---
id: system-service-service
namespace: system:service:service
name: service
description: Run System V init script, can execute commands.
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
  - systemctl
  - rc-service
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
  - service
  - systemctl
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "service /path/to/script start"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via service
    command: service /path/to/script start
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/service/"
techniques:
  - execution
install:
  - method: apt
    package_name: "sysvinit-utils"
    commands:
      - "apt-get install -y sysvinit-utils"
---
