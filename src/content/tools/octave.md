---
id: math-octave-octave
namespace: math:octave:octave
name: octave
description: GNU Octave (MATLAB-like), can execute commands.
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
  - matlab
  - R
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
      description: Octave script output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 64
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 64
  network: none
  disk_io: low
allowed-tools:
  - octave
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "octave -q --eval 'system(\"/bin/sh\")'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via octave
    command: octave -q --eval 'system("/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/octave/"
techniques:
  - execution
install:
  - method: apt
    package_name: "octave"
    commands:
      - "apt-get install -y octave"
---
