---
id: system-time-time
namespace: system:time:time
name: time
description: Measure command execution time; can spawn a shell.
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
- time
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
- requires-root
execution:
  template: time
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: time /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/time/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: time
  commands:
  - apt-get install -y time
---

# time

time is a command-line utility. Time command execution duration; can also spawn an interactive shell.
