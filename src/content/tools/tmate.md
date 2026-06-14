---
id: network-ssh-tmate
namespace: network:ssh:tmate
name: tmate
description: Instant terminal sharing over SSH; can spawn a shell.
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
- tmate
parameters: []
features:
- file-system
- interactive
- network-intensive
- process-manip
- requires-root
execution:
  template: tmate
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: tmate -c /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tmate/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: tmate
  commands:
  - apt-get install -y tmate
---

# tmate

tmate is a command-line utility. Instant terminal sharing via SSH.
