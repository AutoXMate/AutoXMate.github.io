---
id: system-auth-su
namespace: system:auth:su
name: su
description: "Run commands with substitute user credentials; can spawn a shell."
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
- su
parameters: []
features: []
execution:
  template: su
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo)
  command: su -c /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/su/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: shadow-utils
  commands:
  - apt-get install -y shadow-utils
---


# su

su is a command-line utility. Run a shell with substitute user and group IDs.
