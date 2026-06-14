---
id: package-python-pipx
namespace: package:python:pipx
name: pipx
description: Isolated Python app installer, can execute Python code.
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
  - easy_install
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
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
  - pipx
  - pip
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "pipx run /path/to/script.py"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via pipx
    command: pipx run /path/to/script.py
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pipx/"
techniques:
  - execution
install:
  - method: pip
    package_name: "pipx"
    commands:
      - "pip install pipx"
---
