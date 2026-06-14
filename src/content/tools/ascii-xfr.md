---
id: network-transfer-ascii-xfr
namespace: network:transfer:ascii-xfr
name: ascii-xfr
description: Transfer ASCII files using XMODEM protocol, can read arbitrary files via sudo or SUID.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
risk_level: medium
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
  - ascii-xfr
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
  template: "ascii-xfr -ns {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via ascii-xfr
    command: ascii-xfr -ns /path/to/input-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ascii-xfr/"
techniques:
  - collection
  - exfiltration
install:
  - method: apt
    package_name: "minicom"
    commands:
      - "apt-get install -y minicom"
---
