---
id: network-ssh-ssh-agent
namespace: network:ssh:ssh-agent
name: ssh-agent
description: "SSH authentication agent; can spawn a shell."
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
- ssh-agent
parameters: []
features: []
execution:
  template: ssh-agent
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: ssh-agent /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ssh-agent/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---


# ssh-agent

ssh-agent is a command-line utility. SSH authentication agent that can spawn a shell; can also spawn an interactive shell.
