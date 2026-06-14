---
id: text-search-fzf
namespace: text:search:fzf
name: fzf
description: Fuzzy finder, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
  - sk
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or command output
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
  - fzf
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
execution:
  template: "fzf --bind 'x:execute(/bin/sh -c {})'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via fzf
    command: fzf --bind 'x:execute(/bin/sh -c {})'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/fzf/"
techniques:
  - execution
  - collection
install:
  - method: apt
    package_name: "fzf"
    commands:
      - "apt-get install -y fzf"
---
