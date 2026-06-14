---
id: shell-elvish-elvish
namespace: shell:elvish:elvish
name: elvish
description: Expressive shell, can spawn interactive shells and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - bash
  - zsh
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
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - elvish
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "elvish"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via elvish
    command: elvish
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/elvish/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "elvish"
    commands:
      - "apt-get install -y elvish"
---
