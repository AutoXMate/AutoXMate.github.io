---
id: compression-gzip-zcat
namespace: compression:gzip:zcat
name: zcat
description: "Decompress gzipped files to stdout; can read arbitrary files."
author: GTFOBins
version: 1.0.0
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - shell-access
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- zcat
parameters: []
features: []
execution:
  template: zcat
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, unprivileged)
  command: zcat -f /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zcat/
techniques:
- collection
install:
- method: apt
  package_name: gzip
  commands:
  - apt-get install -y gzip
---


# zcat

zcat is a command-line utility. Decompress gzipped files to stdout; can also read arbitrary files.
