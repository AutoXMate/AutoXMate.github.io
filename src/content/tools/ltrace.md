---
id: system-debug-ltrace
namespace: system:debug:ltrace
name: ltrace
description: Library call tracer, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - strace
  - gdb
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - ltrace
  - strace
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "ltrace /path/to/binary"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read file via ltrace
    command: ltrace /path/to/binary
  - description: Execute command via ltrace
    command: ltrace /path/to/binary
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ltrace/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "ltrace"
    commands:
      - "apt-get install -y ltrace"
---
