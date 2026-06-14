---
id: dev-symbol-readelf
namespace: dev:symbol:readelf
name: readelf
description: ELF file reader, can read binary files.
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
  - nm
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - readelf
  - nm
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "readelf -a /path/to/binary"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read an ELF file via readelf
    command: readelf -a /path/to/binary
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/readelf/"
techniques:
  - collection
install:
  - method: apt
    package_name: "binutils"
    commands:
      - "apt-get install -y binutils"
---
