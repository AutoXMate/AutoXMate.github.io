---
id: system-service-fail2ban
namespace: system:service:fail2ban
name: fail2ban-client
description: Fail2ban client, can execute commands via crafted config.
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
  - fail2ban
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
  - fail2ban-client
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "fail2ban-client config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via fail2ban-client
    command: fail2ban-client config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/fail2ban-client/"
techniques:
  - execution
install:
  - method: apt
    package_name: "fail2ban"
    commands:
      - "apt-get install -y fail2ban"
---
