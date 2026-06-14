---
id: system-io-stdbuf
namespace: system:io:stdbuf
name: stdbuf
description: Control standard I/O buffering; can spawn a shell.
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
- stdbuf
parameters: []
features:
- interactive
- process-manip
- requires-root
execution:
  template: stdbuf
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: stdbuf -i0 /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/stdbuf/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: coreutils
  commands:
  - apt-get install -y coreutils
---

# stdbuf

stdbuf is a command-line utility. Control standard I/O buffering for commands; can also spawn an interactive shell.
