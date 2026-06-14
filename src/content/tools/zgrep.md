---
id: system-search-zgrep
namespace: system:search:zgrep
name: zgrep
description: Search gzipped files for patterns; can read arbitrary files.
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
- zgrep
parameters: []
features:
- compression
- file-system
- local
- pipes-stdin
execution:
  template: zgrep
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, unprivileged)
  command: grep '' /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zgrep/
techniques:
- collection
install:
- method: apt
  package_name: gzip
  commands:
  - apt-get install -y gzip
---

# zgrep

zgrep is a command-line utility. Search gzipped files for patterns; can also read arbitrary files.
