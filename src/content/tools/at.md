---
id: system-scheduler-at
namespace: system:scheduler:at
name: at
description: Job scheduler for one-time task execution; can execute arbitrary commands and spawn shells Can also execute arbitrary commands, spawn an interactive shell.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
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
- at
parameters: []
features: []
execution:
  template: at
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands
  command: echo /path/to/command | at now
- description: Spawn an interactive shell
  command: echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | at now; tail -f /dev/null
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/at/
techniques:
- execution
- privilege-escalation
install:
- method: apt
  package_name: at
  commands:
  - apt-get install -y at
---


# at

at is a command-line utility. Job scheduler for one-time task execution; can execute arbitrary commands and spawn shells Can also execute arbitrary commands, spawn an interactive shell.
