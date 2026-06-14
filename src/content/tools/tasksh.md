---
id: system-taskwarrior-tasksh
namespace: system:taskwarrior:tasksh
name: tasksh
description: "Taskwarrior interactive shell; can spawn a shell."
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
- tasksh
parameters: []
features: []
execution:
  template: tasksh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: 'tasksh

    !/bin/sh'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tasksh/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: tasksh
  commands:
  - apt-get install -y tasksh
---


# tasksh

tasksh is a command-line utility. Taskwarrior interactive shell; can also spawn an interactive shell.
