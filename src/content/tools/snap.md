---
id: package-snap-snap
namespace: package:snap:snap
name: snap
description: Snap package manager; can spawn a shell.
author: GTFOBins
version: 1.0.0
capabilities:
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
- snap
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
execution:
  template: snap
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo)
  command: snap install xxxx_1.0_all.snap --dangerous --devmode
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/snap/
techniques:
- execution
install:
- method: apt
  package_name: snapd
  commands:
  - apt-get install -y snapd
---

# snap

snap is a command-line utility. Snap package manager; can also execute arbitrary commands.
