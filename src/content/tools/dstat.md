---
id: system-monitor-dstat
namespace: system:monitor:dstat
name: dstat
description: System resource statistics tool, can execute Python code via external plugins.
author: "GTFOBins"
version: "1.0.0"
capabilities:
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
      description: Python code execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - dstat
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "dstat --xxx"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via dstat plugin
    command: dstat --xxx
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dstat/"
techniques:
  - execution
install:
  - method: apt
    package_name: "dstat"
    commands:
      - "apt-get install -y dstat"
---
