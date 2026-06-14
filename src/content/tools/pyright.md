---
id: dev-typing-pyright
namespace: dev:typing:pyright
name: pyright
description: Python type checker (Node.js), can execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - mypy
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
  - pyright
  - mypy
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "pyright /path/to/script.py"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via pyright
    command: pyright /path/to/script.py
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pyright/"
techniques:
  - execution
install:
  - method: npm
    package_name: "pyright"
    commands:
      - "npm install -g pyright"
---
