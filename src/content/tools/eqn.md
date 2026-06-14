---
id: text-format-eqn
namespace: text:format:eqn
name: eqn
description: Equation formatter for troff, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
  - troff
  - groff
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - eqn
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "eqn /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via eqn
    command: eqn /path/to/file
  - description: Execute command via eqn
    command: eqn /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/eqn/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "groff-base"
    commands:
      - "apt-get install -y groff-base"
---
