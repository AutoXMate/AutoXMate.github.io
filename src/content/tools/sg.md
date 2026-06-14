---
id: system-group-sg
namespace: system:group:sg
name: sg
description: Execute command with a different group ID; can spawn an interactive shell.
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
- sg
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
- requires-root
execution:
  template: sg
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: sg $(id -ng)
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sg/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: shadow-utils
  commands:
  - apt-get install -y shadow-utils
---

# sg

sg is a command-line utility. Switch group ID utility that can spawn a shell; can also spawn an interactive shell.
