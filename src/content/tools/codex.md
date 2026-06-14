---
id: dev-nix-codex
namespace: dev:nix:codex
name: codex
description: Nix-based development environment tool, can spawn a shell via codex sandbox.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools: []
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - codex
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "codex sandbox linux /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via codex sandbox
    command: codex sandbox linux /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/codex/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: pip
    package_name: "codex"
    commands:
      - "pip install codex"
---
