---
id: package-python-pip
namespace: package:python:pip
name: pip
description: Python package installer, can execute Python code via setup.py.
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
  - pipx
  - easy_install
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
  - pip
  - pipx
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "pip install /path/to/package"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via pip install
    command: pip install /path/to/package
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pip/"
techniques:
  - execution
install:
  - method: pip
    package_name: "pip"
    commands:
      - "pip install pip"
---
