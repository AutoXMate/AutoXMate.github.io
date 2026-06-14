---
id: security-sandbox-genie
namespace: security:sandbox:genie
name: genie
description: Sandbox wrapper for systemd, can execute commands and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - systemd-run
  - nsenter
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - genie
  - nsenter
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "genie -c /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via genie
    command: genie -c /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/genie/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "genie"
    commands:
      - "apt-get install -y genie"
---
