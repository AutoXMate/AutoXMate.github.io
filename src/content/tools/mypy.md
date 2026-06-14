---
id: dev-typing-mypy
namespace: dev:typing:mypy
name: mypy
description: Python type checker, can execute Python code via plugins.
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
  - python
  - pyright
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - mypy
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "mypy /path/to/script.py"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via mypy
    command: mypy /path/to/script.py
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/mypy/"
techniques:
  - execution
install:
  - method: pip
    package_name: "mypy"
    commands:
      - "pip install mypy"
---
