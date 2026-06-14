---
id: shell-sash-sash
namespace: shell:sash:sash
name: sash
description: Stand-alone shell with built-in commands, can spawn interactive shells.
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
  - sash
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "sash"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via sash
    command: sash
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/sash/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "sash"
    commands:
      - "apt-get install -y sash"
---
