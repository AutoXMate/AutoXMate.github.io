---
id: text-convert-dos2unix
namespace: text:convert:dos2unix
name: dos2unix
description: Convert text file line endings, can read and write files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
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
  - unix2dos
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - dos2unix
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "dos2unix -f -O {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via dos2unix
    command: dos2unix -f -O /path/to/input-file
  - description: Write to a file via dos2unix
    command: dos2unix -f -n /path/to/input-file /path/to/output-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dos2unix/"
techniques:
  - collection
install:
  - method: apt
    package_name: "dos2unix"
    commands:
      - "apt-get install -y dos2unix"
---
