---
id: system-process-choom
namespace: system:process:choom
name: choom
description: Display and adjust OOM killer score, can spawn a shell via -n flag.
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
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
- choom
- Bash
- execFile
parameters: []
features:
- process-manip
execution:
  template: choom -n 0 /bin/sh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn a shell via choom
  command: choom -n 0 /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/choom/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: util-linux
  commands:
  - apt-get install -y util-linux
mitre_ids:
- T1059
---


