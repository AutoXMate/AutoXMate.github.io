---
id: system-debug-gdb
namespace: system:debug:gdb
name: gdb
description: GNU debugger, can execute commands via Python scripting.
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
  - gcore
  - python
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - gdb
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
  - interactive
execution:
  template: "gdb -batch -ex 'python import os; os.system(\"/bin/sh\")'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via gdb Python integration
    command: gdb -batch -ex 'python import os; os.system("/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/gdb/"
techniques:
  - execution
install:
  - method: apt
    package_name: "gdb"
    commands:
      - "apt-get install -y gdb"
---
