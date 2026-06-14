---
id: system-container-chroot
namespace: system:container:chroot
name: chroot
description: Run command or shell with a different root directory, can spawn a privileged shell with SUID.
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
  - arch-nspawn
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
  - chroot
  - Bash
  - execFile
parameters:
  - name: directory
    type: string
    required: false
    description: "Root directory for chroot"
features:
  - process-manip
execution:
  template: "chroot {directory} /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via chroot
    command: chroot /
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/chroot/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "coreutils"
    commands:
      - "apt-get install -y coreutils"
---
