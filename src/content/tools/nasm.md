---
id: build-assembler-nasm
namespace: build:assembler:nasm
name: nasm
description: Netwide Assembler, can execute commands via compiled binaries.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - as
  - ld
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
      description: Binary execution output
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
  - nasm
  - as
  - ld
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "nasm -f bin /path/to/input.asm -o /path/to/output"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via nasm
    command: nasm -f bin /path/to/input.asm -o /path/to/output
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nasm/"
techniques:
  - execution
install:
  - method: apt
    package_name: "nasm"
    commands:
      - "apt-get install -y nasm"
---
