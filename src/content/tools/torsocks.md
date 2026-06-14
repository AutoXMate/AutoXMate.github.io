---
id: network-proxy-torsocks
namespace: network:proxy:torsocks
name: torsocks
description: Run commands through Tor (legacy wrapper); can spawn a shell.
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
- torsocks
parameters: []
features:
- interactive
- network-intensive
- process-manip
- remote
- requires-root
execution:
  template: torsocks
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: torsocks /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/torsocks/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: tor
  commands:
  - apt-get install -y tor
---

# torsocks

torsocks is a command-line utility. Run commands through the Tor network (deprecated); can also spawn an interactive shell.
