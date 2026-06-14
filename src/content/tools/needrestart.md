---
id: system-package-needrestart
namespace: system:package:needrestart
name: needrestart
description: Check for processes needing restart after updates, can execute commands.
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - needrestart
  - Bash
  - execFile
parameters: []
features:
  - process-manip
  - requires-root
execution:
  template: "needrestart -r /path/to/hook"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via needrestart
    command: needrestart -r /path/to/hook
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/needrestart/"
techniques:
  - execution
install:
  - method: apt
    package_name: "needrestart"
    commands:
      - "apt-get install -y needrestart"
---
