---
id: system-mime-run-mailcap
namespace: system:mime:run-mailcap
name: run-mailcap
description: Run program via mailcap entries, can execute commands.
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
related_tools: []
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
  - run-mailcap
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "run-mailcap /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via run-mailcap
    command: run-mailcap /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/run-mailcap/"
techniques:
  - execution
install:
  - method: apt
    package_name: "mime-support"
    commands:
      - "apt-get install -y mime-support"
---
