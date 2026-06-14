---
id: dev-symbol-nm
namespace: dev:symbol:nm
name: nm
description: List symbols from object files, can read files.
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
  - readelf
  - objdump
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
  side_effects: []
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
  - nm
  - readelf
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "nm /path/to/binary"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read symbols via nm
    command: nm /path/to/binary
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nm/"
techniques:
  - collection
install:
  - method: apt
    package_name: "binutils"
    commands:
      - "apt-get install -y binutils"
---
