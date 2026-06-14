---
id: shell-fish
namespace: shell:interactive:fish
name: fish
description: Friendly interactive shell with advanced features, can be used for privilege escalation.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
  - macos
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - bash
  - zsh
  - ash
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - fish
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "fish"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive fish shell
    command: fish
references:
  - label: "fish shell documentation"
    url: "https://fishshell.com/docs/current/"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "fish"
      commands:
        - "apt-get install -y fish"
---


# fish — Friendly Interactive Shell

fish is a smart, user-friendly command-line shell. When installed with SUID or available via sudo, it spawns an interactive shell with the privileges of the file owner.
