---
id: text-troff-nroff
namespace: text:troff:nroff
name: nroff
description: Troff formatter, can read files and execute commands.
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
  - troff
  - groff
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
  - nroff
  - troff
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "nroff /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via nroff
    command: nroff /path/to/file
  - description: Execute command via nroff
    command: nroff /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nroff/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "groff-base"
    commands:
      - "apt-get install -y groff-base"
---
