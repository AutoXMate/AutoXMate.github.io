---
id: system-file-batcat
namespace: system:file:batcat
name: batcat
description: A cat(1) clone with syntax highlighting, can read files via pager (less) inheritance.
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
  - cat
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
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - batcat
  - less
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read"
features:
  - file-system
  - pipes-stdout
execution:
  template: "batcat --paging always {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via batcat (pager mode)
    command: batcat --paging always /etc/hosts
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/batcat/"
techniques:
  - collection
install:
  - method: apt
    package_name: "bat"
    commands:
      - "apt-get install -y bat"
  - method: brew
    package_name: "bat"
    commands:
      - "brew install bat"
---
