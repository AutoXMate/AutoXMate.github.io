---
id: dev-debug-valgrind
namespace: dev:debug:valgrind
name: valgrind
description: "Memory debugging and profiling tool; can read arbitrary files."
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
- valgrind
parameters: []
features: []
execution:
  template: valgrind
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: valgrind /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/valgrind/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: valgrind
  commands:
  - apt-get install -y valgrind
---


# valgrind

valgrind is a command-line utility. Memory debugging, leak detection, and profiling tool; can also spawn an interactive shell.
