---
id: system-debug-scanmem
namespace: system:debug:scanmem
name: scanmem
description: Memory scanner, can read process memory.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - bsd
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - gdb
  - gcore
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
      description: Memory read output
  side_effects: []
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
  - scanmem
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "scanmem -p <pid>"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read process memory via scanmem
    command: scanmem -p <pid>
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/scanmem/"
techniques:
  - collection
install:
  - method: apt
    package_name: "scanmem"
    commands:
      - "apt-get install -y scanmem"
---
