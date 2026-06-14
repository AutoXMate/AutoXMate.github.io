---
id: text-awk-nawk
namespace: text:awk:nawk
name: nawk
description: New awk, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
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
  - awk
  - gawk
  - mawk
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or command output
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
  - nawk
  - awk
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "nawk 'BEGIN {system(\"/bin/sh\")}'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via nawk
    command: nawk 'BEGIN {system("/bin/sh")}'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nawk/"
techniques:
  - execution
  - collection
install:
  - method: apt
    package_name: "original-awk"
    commands:
      - "apt-get install -y original-awk"
---
