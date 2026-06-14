---
id: system-taskwarrior-task
namespace: system:taskwarrior:task
name: task
description: "Taskwarrior task management tool; can read and write files and spawn shells."
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
- task
parameters: []
features: []
execution:
  template: task
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: task execute /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/task/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: task
  commands:
  - apt-get install -y task
---


# task

task is a command-line utility. Taskwarrior task management tool; can also spawn an interactive shell.
