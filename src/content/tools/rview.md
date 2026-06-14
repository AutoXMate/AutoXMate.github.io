---
id: text-editor-rview
namespace: text:editor:rview
name: rview
description: Restricted view (vim in restricted mode), can spawn a shell via ! command.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
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
  - rvim
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or file output
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
  - rview
  - vi
  - vim
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "rview /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via rview
    command: |
      rview /path/to/file
      :!/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rview/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "vim-common"
    commands:
      - "apt-get install -y vim-common"
---
