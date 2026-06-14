---
id: system-file-cmp
namespace: system:file:cmp
name: cmp
description: Compare two files byte by byte, can read files via byte comparison with /dev/zero.
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
related_tools:
  - diff
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
      description: File content
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
  - cmp
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read"
features: []
execution:
  template: "cmp {input} /dev/zero -b -l"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via cmp byte comparison
    command: cmp /path/to/input-file /dev/zero -b -l
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cmp/"
techniques:
  - collection
install:
  - method: apt
    package_name: "diffutils"
    commands:
      - "apt-get install -y diffutils"
---
