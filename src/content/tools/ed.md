---
id: text-editor-ed
namespace: text:editor:ed
name: ed
description: Line-oriented text editor, can spawn a shell via ! command.
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
  - ed
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "ed /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ed
    command: |
      ed
      !/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ed/"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
  - method: apt
    package_name: "ed"
    commands:
      - "apt-get install -y ed"
---
