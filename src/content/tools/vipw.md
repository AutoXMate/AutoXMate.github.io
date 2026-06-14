---
id: system-auth-vipw
namespace: system:auth:vipw
name: vipw
description: "Edit password file with safe locking; can spawn a shell."
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
- vipw
parameters: []
features: []
execution:
  template: vipw
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage vi capabilities
  command: vipw
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/vipw/
techniques:
- execution
install:
- method: apt
  package_name: shadow-utils
  commands:
  - apt-get install -y shadow-utils
---


# vipw

vipw is a command-line utility. Edit password file with locking Can leverage capabilities from: vi.
