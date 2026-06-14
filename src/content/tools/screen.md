---
id: system-terminal-screen
namespace: system:terminal:screen
name: screen
description: Terminal multiplexer, can spawn shells and read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
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
  - tmux
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or file output
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
  - screen
  - tmux
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - file-system
  - process-manip
execution:
  template: "screen /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via screen
    command: screen /bin/sh
  - description: Read a file via screen
    command: screen /bin/cat /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/screen/"
techniques:
  - privilege-escalation
  - collection
install:
  - method: apt
    package_name: "screen"
    commands:
      - "apt-get install -y screen"
---
