---
id: package-rpm-rpmquery
namespace: package:rpm:rpmquery
name: rpmquery
description: RPM package query tool, can read files.
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
  - rpmdb
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
  - rpmquery
  - rpm
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "rpmquery /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via rpmquery
    command: rpmquery /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rpmquery/"
techniques:
  - collection
install:
  - method: apt
    package_name: "rpm"
    commands:
      - "apt-get install -y rpm"
---
