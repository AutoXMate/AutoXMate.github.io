---
id: system-scheduler-run-parts
namespace: system:scheduler:run-parts
name: run-parts
description: Run scripts in a directory, can execute commands.
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
  - crontab
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
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - run-parts
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "run-parts /path/to/dir"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute commands in a directory
    command: run-parts /path/to/dir
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/run-parts/"
techniques:
  - execution
install:
  - method: apt
    package_name: "debianutils"
    commands:
      - "apt-get install -y debianutils"
---
