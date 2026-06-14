---
id: lang-haskell-ghci
namespace: lang:haskell:ghci
name: ghci
description: Glasgow Haskell Compiler interactive, can execute code and spawn shells.
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
  - ghc
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
  - ghci
  - ghc
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "ghci -e 'System.Posix.Process.executeFile \"/bin/sh\" False [] Nothing'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ghci
    command: ghci -e 'System.Posix.Process.executeFile "/bin/sh" False [] Nothing'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ghci/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "ghc"
    commands:
      - "apt-get install -y ghc"
---
