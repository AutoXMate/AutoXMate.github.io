---
id: network-remote-rlogin
namespace: network:remote:rlogin
name: rlogin
description: Remote login client, can execute commands.
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
  - ssh
  - telnet
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
      description: Remote command output
  side_effects:
    - network_traffic
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - rlogin
  - ssh
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "rlogin /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via rlogin
    command: rlogin /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rlogin/"
techniques:
  - execution
install:
  - method: apt
    package_name: "rsh-client"
    commands:
      - "apt-get install -y rsh-client"
---
