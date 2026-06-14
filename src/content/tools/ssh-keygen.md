---
id: network-ssh-ssh-keygen
namespace: network:ssh:ssh-keygen
name: ssh-keygen
description: SSH key generation and management; can read and write files.
author: GTFOBins
version: 1.0.0
capabilities:
- system.library.load
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
- ssh-keygen
parameters: []
features:
- file-system
- local
- network-intensive
execution:
  template: ssh-keygen
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Load arbitrary libraries (sudo, suid, unprivileged)
  command: ssh-keygen -D /path/to/lib.so
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ssh-keygen/
techniques:
- execution
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---

# ssh-keygen

ssh-keygen is a command-line utility. SSH key generation and management utility.
