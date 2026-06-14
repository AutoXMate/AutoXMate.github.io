---
id: system-filesystem-debugfs
namespace: system:filesystem:debugfs
name: debugfs
description: ext2/ext3/ext4 filesystem debugger, can spawn a shell from the debugger CLI.
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
  - debugfs
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "debugfs"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell from the debugfs CLI
    command: |
      debugfs
      !/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/debugfs/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "e2fsprogs"
    commands:
      - "apt-get install -y e2fsprogs"
---
