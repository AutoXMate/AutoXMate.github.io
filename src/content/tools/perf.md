---
id: system-benchmark-perf
namespace: system:benchmark:perf
name: perf
description: Performance analysis tool, can execute commands via probe events.
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
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - perf
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "perf stat /path/to/command"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via perf
    command: perf stat /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/perf/"
techniques:
  - execution
install:
  - method: apt
    package_name: "linux-tools-common"
    commands:
      - "apt-get install -y linux-tools-common"
---
