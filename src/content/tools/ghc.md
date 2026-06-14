---
id: lang-haskell-ghc
namespace: lang:haskell:ghc
name: ghc
description: Glasgow Haskell Compiler, can execute code and spawn shells via compiled binaries.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - ghci
  - runghc
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
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
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - ghc
  - ghci
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "ghc -e 'System.Posix.Process.executeFile \"/bin/sh\" False [] Nothing'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ghc
    command: ghc -e 'System.Posix.Process.executeFile "/bin/sh" False [] Nothing'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ghc/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "ghc"
    commands:
      - "apt-get install -y ghc"
---
