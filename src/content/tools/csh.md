---
id: shell-csh-csh
namespace: shell:csh:csh
name: csh
description: C shell, can spawn interactive shells and write files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.write
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
related_tools:
  - bash
  - sh
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
    - filesystem_write
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
  - csh
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "csh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive C shell
    command: csh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/csh/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "csh"
    commands:
      - "apt-get install -y csh"
---
