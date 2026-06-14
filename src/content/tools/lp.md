---
id: system-print-lp
namespace: system:print:lp
name: lp
description: Print files, can read and write files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
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
  - cancel
  - lpstat
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
  - lp
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "lp -d /path/to/output /path/to/input"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via lp
    command: lp -d /path/to/output /path/to/input
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/lp/"
techniques:
  - collection
install:
  - method: apt
    package_name: "cups"
    commands:
      - "apt-get install -y cups"
---
