---
id: network-socket-ss
namespace: network:socket:ss
name: ss
description: "Socket statistics utility; can read remote files via TCP."
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
- ss
parameters: []
features: []
execution:
  template: ss
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: ss -a -F /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ss/
techniques:
- collection
install:
- method: apt
  package_name: iproute2
  commands:
  - apt-get install -y iproute2
---


# ss

ss is a command-line utility. Socket statistics utility; can be used to read remote files via TCP.
