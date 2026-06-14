---
id: encode-base-base58
namespace: encode:base:base58
name: base58
description: Base58 encoding/decoding utility, can read files via sudo.
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
related_tools:
  - base64
  - base32
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
  - base58
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
  template: "base58 {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via base58
    command: base58 /path/to/input-file | base58 --decode
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/base58/"
techniques:
  - collection
  - exfiltration
install:
  - method: apt
    package_name: "base58"
    commands:
      - "apt-get install -y base58"
---
