---
id: dev-python-pdb
namespace: dev:python:pdb
name: pdb
description: Python debugger, can execute Python code and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - gdb
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Python debugger output
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
  - pdb
  - python
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "python -m pdb /path/to/script.py"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via pdb
    command: python -m pdb /path/to/script.py
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pdb/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "python3"
    commands:
      - "apt-get install -y python3"
---
