---
id: system-resource-softlimit
namespace: system:resource:softlimit
name: softlimit
description: "Set soft resource limits for commands; can spawn a shell."
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
- softlimit
parameters: []
features: []
execution:
  template: softlimit
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: softlimit /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/softlimit/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: daemontools
  commands:
  - apt-get install -y daemontools
---


# softlimit

softlimit is a command-line utility. Set soft resource limits for a command; can also spawn an interactive shell.
