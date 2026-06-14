---
id: encode-ascii-atobm
namespace: encode:ascii:atobm
name: atobm
description: Convert ASCII text to PBM bitmap format, can read files via sudo or SUID.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs:
    - type: system.file.path
      description: Path to input file
  outputs:
    - type: process.output
      description: File content output
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
  - atobm
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read"
features:
  - file-system
execution:
  template: "atobm {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via atobm
    command: atobm /path/to/input-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/atobm/"
techniques:
  - collection
install:
  - method: apt
    package_name: "netpbm"
    commands:
      - "apt-get install -y netpbm"
---
