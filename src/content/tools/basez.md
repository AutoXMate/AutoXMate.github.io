---
id: encode-base-basez
namespace: encode:base:basez
name: basez
description: Extended base encoding/decoding utility, can read files via sudo or SUID.
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
  - base64
  - base32
  - basenc
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
      description: Encoded file content
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
  - basez
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
  template: "basez {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via basez
    command: basez /path/to/input-file | basez --decode
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/basez/"
techniques:
  - collection
  - exfiltration
install:
  - method: apt
    package_name: "basez"
    commands:
      - "apt-get install -y basez"
---
