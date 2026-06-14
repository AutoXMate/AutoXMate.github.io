---
id: network-diagnostic-mtr
namespace: network:diagnostic:mtr
name: mtr
description: Network diagnostic tool combining traceroute and ping, can read files.
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
  - traceroute
  - ping
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
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - mtr
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - requires-root
execution:
  template: "mtr /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via mtr
    command: mtr /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/mtr/"
techniques:
  - collection
install:
  - method: apt
    package_name: "mtr"
    commands:
      - "apt-get install -y mtr"
---
