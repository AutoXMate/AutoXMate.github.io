---
id: network-proxy-torify
namespace: network:proxy:torify
name: torify
description: "Run commands through the Tor anonymizing network; can spawn a shell."
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
- torify
parameters: []
features: []
execution:
  template: torify
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: torify /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/torify/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: tor
  commands:
  - apt-get install -y tor
---


# torify

torify is a command-line utility. Run a command through the Tor network.
