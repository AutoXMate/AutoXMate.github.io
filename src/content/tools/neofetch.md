---
id: system-info-neofetch
namespace: system:info:neofetch
name: neofetch
description: System info display, can execute commands via custom config.
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
  - fastfetch
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
  - neofetch
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "neofetch --config /path/to/config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via neofetch config
    command: neofetch --config /path/to/config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/neofetch/"
techniques:
  - execution
install:
  - method: apt
    package_name: "neofetch"
    commands:
      - "apt-get install -y neofetch"
---
