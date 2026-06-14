---
id: system-process-cpulimit
namespace: system:process:cpulimit
name: cpulimit
description: Limit CPU usage of a process, can spawn a shell via cpulimit.
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
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
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
  - cpulimit
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "cpulimit -l 100 -f -- /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via cpulimit
    command: cpulimit -l 100 -f -- /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cpulimit/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "cpulimit"
    commands:
      - "apt-get install -y cpulimit"
---
