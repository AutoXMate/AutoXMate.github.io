---
id: system-file-install
namespace: system:file:install
name: install
description: Copy files and set attributes, can read and write files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
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
  - cp
  - mv
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
    - filesystem_write
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - install
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "install -m 755 /path/to/input /path/to/output"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via install
    command: install -m 755 /path/to/input /path/to/output
  - description: Execute command via install
    command: install -m 755 /path/to/input /path/to/output
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/install/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "coreutils"
    commands:
      - "apt-get install -y coreutils"
---
