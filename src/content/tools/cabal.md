---
id: dev-haskell-cabal
namespace: dev:haskell:cabal
name: cabal
description: Haskell package build system, can spawn shells via cabal exec with project-file option.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
  - macos
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
  inputs:
    - type: security.execution.context
      description: Sudo, SUID, or unprivileged execution context
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - cabal
  - ghc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "cabal exec --project-file=/dev/null -- /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via cabal exec
    command: cabal exec --project-file=/dev/null -- /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cabal/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "cabal-install"
    commands:
      - "apt-get install -y cabal-install"
---
