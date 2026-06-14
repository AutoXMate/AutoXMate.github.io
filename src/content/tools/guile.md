---
id: lang-scheme-guile
namespace: lang:scheme:guile
name: guile
description: GNU Guile Scheme interpreter, can execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
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
  - ginsh
artifacts: []
workflow_edges:
  produces:
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Scheme script output
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
  - guile
  - Bash
  - execFile
parameters: []
features:
  - process-manip
  - interactive
execution:
  template: "guile -c '(system \"/bin/sh\")'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via guile
    command: guile -c '(system "/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/guile/"
techniques:
  - execution
install:
  - method: apt
    package_name: "guile-3.0"
    commands:
      - "apt-get install -y guile-3.0"
---
