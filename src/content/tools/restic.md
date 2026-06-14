---
id: backup-restic-restic
namespace: backup:restic:restic
name: restic
description: Backup tool, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - borg
  - rsync
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
    - network_traffic
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
  - restic
  - borg
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "restic backup /path/to/dir"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via restic
    command: restic backup /path/to/dir
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/restic/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "restic"
    commands:
      - "apt-get install -y restic"
---
