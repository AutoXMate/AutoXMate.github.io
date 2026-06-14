---
id: system-file-ranger
namespace: system:file:ranger
name: ranger
description: File manager, can read files and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.privilege-escalation.shell
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
  - mc
  - nnn
artifacts: []
workflow_edges:
  produces:
    - file-content
    - shell-access
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or shell output
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
  - ranger
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - file-system
  - process-manip
execution:
  template: "ranger /path/to/dir"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ranger
    command: |
      ranger
      :shell /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ranger/"
techniques:
  - privilege-escalation
  - collection
install:
  - method: pip
    package_name: "ranger-fm"
    commands:
      - "pip install ranger-fm"
---
