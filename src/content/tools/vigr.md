---
id: system-auth-vigr
namespace: system:auth:vigr
name: vigr
description: "Edit group file with safe locking; can spawn a shell."
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
- vigr
parameters: []
features: []
execution:
  template: vigr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage vi capabilities
  command: vigr
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/vigr/
techniques:
- execution
install:
- method: apt
  package_name: shadow-utils
  commands:
  - apt-get install -y shadow-utils
---


# vigr

vigr is a command-line utility. Edit group file with locking Can leverage capabilities from: vi.
