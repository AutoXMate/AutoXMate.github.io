---
id: text-editor-rvim
namespace: text:editor:rvim
name: rvim
description: Restricted vim, can spawn a shell via ! command.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - vi
  - vim
  - rview
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
  - rvim
  - vi
  - vim
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "rvim /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via rvim
    command: |
      rvim /path/to/file
      :!/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rvim/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "vim-common"
    commands:
      - "apt-get install -y vim-common"
---
