---
id: communication-voip-asterisk
namespace: communication:voip:asterisk
name: asterisk
description: Asterisk PBX remote console, can spawn a shell from the CLI when running as root or via sudo/SUID.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or SUID execution context
  outputs:
    - type: process.output
      description: Shell output
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
  - asterisk
  - Bash
  - execFile
parameters:
  - name: args
    type: string
    required: false
    description: "CLI arguments for asterisk"
features:
  - interactive
  - process-manip
execution:
  template: "asterisk -r"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive shell from the Asterisk CLI
    command: |
      asterisk -r
      !/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/asterisk/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "asterisk"
    commands:
      - "apt-get install -y asterisk"
---
