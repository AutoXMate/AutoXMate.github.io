---
id: network-time-ntpdate
namespace: network:time:ntpdate
name: ntpdate
description: Set system time from NTP server, can execute commands.
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - ntpdate
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "ntpdate /path/to/config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via ntpdate
    command: ntpdate /path/to/config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ntpdate/"
techniques:
  - execution
install:
  - method: apt
    package_name: "ntpdate"
    commands:
      - "apt-get install -y ntpdate"
---
