---
id: package-python-easy-install
namespace: package:python:easy-install
name: easy_install
description: Python package installer (setuptools), can execute Python code via setup.py.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - macos
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
    - filesystem_write
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
  - easy_install
  - pip
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "easy_install ."
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via easy_install setup.py
    command: |
      echo 'import os; os.system("exec /bin/sh </dev/tty >/dev/tty 2>/dev/tty")' >setup.py
      easy_install .
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/easy_install/"
techniques:
  - execution
install:
  - method: pip
    package_name: "setuptools"
    commands:
      - "pip install setuptools"
---
