---
id: system-library-ldso
namespace: system:library:ldso
name: ld.so
description: Dynamic linker/loader, can execute arbitrary shared objects.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - ldconfig
  - gcc
artifacts: []
workflow_edges:
  produces:
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - ld.so
  - ldconfig
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "ld.so /path/to/binary"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via ld.so
    command: ld.so /path/to/binary
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ld.so/"
techniques:
  - execution
install:
  - method: apt
    package_name: "libc-bin"
    commands:
      - "apt-get install -y libc-bin"
---
