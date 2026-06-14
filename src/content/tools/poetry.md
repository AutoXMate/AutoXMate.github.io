---
id: dev-python-poetry
namespace: dev:python:poetry
name: poetry
description: Python dependency manager, can execute Python code via scripts.
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
  - pip
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - poetry
  - pip
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "poetry run /path/to/script"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via poetry
    command: poetry run /path/to/script
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/poetry/"
techniques:
  - execution
install:
  - method: pip
    package_name: "poetry"
    commands:
      - "pip install poetry"
---
