---
id: system-test-gtester
namespace: system:test:gtester
name: gtester
description: GLib test runner, can execute commands via test paths.
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - gtester
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "gtester /path/to/test"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via gtester
    command: gtester /path/to/test
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/gtester/"
techniques:
  - execution
install:
  - method: apt
    package_name: "libglib2.0-bin"
    commands:
      - "apt-get install -y libglib2.0-bin"
---
