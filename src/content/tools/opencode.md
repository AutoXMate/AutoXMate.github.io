---
id: dev-opencode-opencode
namespace: dev:opencode:opencode
name: opencode
description: File manager/launcher for Haiku OS; can execute commands and leverage
  sqlite3.
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
- opencode
parameters: []
features:
- file-system
- local
- pipes-stdin
- process-manip
execution:
  template: opencode
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo, suid, unprivileged)
  command: 'opencode

    ! /path/to/command'
- description: Leverage sqlite3 capabilities
  command: opencode db '...'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/opencode/
techniques:
- execution
install:
- method: apt
  package_name: opencode
  commands:
  - apt-get install -y opencode
---

# opencode

opencode is a command-line utility. Open-source AI coding assistant CLI; can also execute arbitrary commands Can also leverage capabilities from: sqlite3.
