---
id: build-distcc-distcc
namespace: build:distcc:distcc
name: distcc
description: Distributed C compiler, can spawn a shell by passing /bin/sh as the compiler.
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
related_tools:
  - gcc
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
  - distcc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "distcc /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via distcc
    command: distcc /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/distcc/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "distcc"
    commands:
      - "apt-get install -y distcc"
---
