---
id: shell-powershell-posh
namespace: shell:powershell:posh
name: posh
description: PowerShell Core, can execute PowerShell commands and spawn shells.
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
  - pwsh
  - powershell
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
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - posh
  - pwsh
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "posh -c 'Start-Process /bin/sh'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via posh
    command: posh -c 'Start-Process /bin/sh'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/posh/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "powershell"
    commands:
      - "apt-get install -y powershell"
---
