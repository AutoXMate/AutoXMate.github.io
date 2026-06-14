---
id: network-ssh-ssh-keyscan
namespace: network:ssh:ssh-keyscan
name: ssh-keyscan
description: "Gather SSH host public keys from remote servers."
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
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
- ssh-keyscan
parameters: []
features: []
execution:
  template: ssh-keyscan
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: ssh-keyscan -f /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ssh-keyscan/
techniques:
- collection
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---


# ssh-keyscan

ssh-keyscan is a command-line utility. Gather SSH host public keys from remote servers.
