---
id: text-editor-ex
namespace: text:editor:ex
name: ex
description: Line-oriented text editor (vi's ancestor), can spawn a shell via ! command.
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
  - ed
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
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - ex
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "ex /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ex
    command: |
      ex
      !/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ex/"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
  - method: apt
    package_name: "vim-common"
    commands:
      - "apt-get install -y vim-common"
---
