---
id: network-email-procmail
namespace: network:email:procmail
name: procmail
description: Mail processing tool, can execute commands via recipes.
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
  - mutt
  - mail
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
  - procmail
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "procmail /path/to/rcfile"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via procmail recipe
    command: procmail /path/to/rcfile
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/procmail/"
techniques:
  - execution
install:
  - method: apt
    package_name: "procmail"
    commands:
      - "apt-get install -y procmail"
---
