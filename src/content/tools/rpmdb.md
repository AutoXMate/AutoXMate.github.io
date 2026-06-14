---
id: package-rpm-rpmdb
namespace: package:rpm:rpmdb
name: rpmdb
description: RPM database query tool, can read files.
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
  - rpm
  - rpmquery
  - rpmverify
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
  - rpmdb
  - rpm
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "rpmdb /path/to/db"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via rpmdb
    command: rpmdb /path/to/db
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rpmdb/"
techniques:
  - collection
install:
  - method: apt
    package_name: "rpm"
    commands:
      - "apt-get install -y rpm"
---
