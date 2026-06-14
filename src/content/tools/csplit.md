---
id: system-file-csplit
namespace: system:file:csplit
name: csplit
description: Split files based on context, can read and write files via sudo or SUID.
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
related_tools: []
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
  - csplit
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "csplit {input} 1"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via csplit
    command: |
      csplit /path/to/input-file 1
      cat xx01
  - description: Write to a file via csplit
    command: |
      echo DATA >/path/to/temp-file
      csplit -z -b '%doutput-file' /path/to/temp-file 1
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/csplit/"
techniques:
  - collection
install:
  - method: apt
    package_name: "coreutils"
    commands:
      - "apt-get install -y coreutils"
---
