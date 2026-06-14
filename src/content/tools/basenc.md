---
id: encode-base-basenc
namespace: encode:base:basenc
name: basenc
description: Base encoding/decoding utility from coreutils, can read files via sudo or SUID.
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
  - base58
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
  - basenc
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read"
  - name: encoding
    type: string
    required: false
    description: "Encoding type (e.g. --base64)"
features:
  - file-system
execution:
  template: "basenc {encoding} {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via basenc with base64 encoding
    command: basenc --base64 /path/to/input-file | basenc -d --base64
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/basenc/"
techniques:
  - collection
  - exfiltration
install:
  - method: apt
    package_name: "coreutils"
    commands:
      - "apt-get install -y coreutils"
---
