---
id: system-file-ncdu
namespace: system:file:ncdu
name: ncdu
description: NCurses disk usage analyzer, can read files.
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
  - du
  - dust
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
  - ncdu
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
execution:
  template: "ncdu /path/to/dir"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read directory info via ncdu
    command: ncdu /path/to/dir
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ncdu/"
techniques:
  - collection
install:
  - method: apt
    package_name: "ncdu"
    commands:
      - "apt-get install -y ncdu"
---
