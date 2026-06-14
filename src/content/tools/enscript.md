---
id: text-print-enscript
namespace: text:print:enscript
name: enscript
description: Convert text files to PostScript, can read files and execute commands.
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
  - a2ps
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
  - enscript
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "enscript /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via enscript
    command: enscript /path/to/file
  - description: Execute command via enscript
    command: enscript /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/enscript/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "enscript"
    commands:
      - "apt-get install -y enscript"
---
