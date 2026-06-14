---
id: system-debug-gcore
namespace: system:debug:gcore
name: gcore
description: Core dump generator, can read process memory and files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
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
  - gdb
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects:
    - filesystem_write
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
  - gcore
  - gdb
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "gcore -o /path/to/output <pid>"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read process memory via gcore
    command: gcore -o /path/to/output <pid>
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/gcore/"
techniques:
  - collection
install:
  - method: apt
    package_name: "gdb"
    commands:
      - "apt-get install -y gdb"
---
