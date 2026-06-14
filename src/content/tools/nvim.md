---
id: text-editor-nvim
namespace: text:editor:nvim
name: nvim
description: Neovim, can spawn a shell via :! or :terminal command.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
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
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - nvim
  - vim
  - vi
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "nvim -c '!/bin/sh'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via nvim
    command: |
      nvim
      :!/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nvim/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "neovim"
    commands:
      - "apt-get install -y neovim"
---
