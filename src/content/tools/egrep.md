---
id: system-search-egrep
namespace: system:search:egrep
name: egrep
description: Extended grep for pattern searching in files; can read arbitrary files.
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
- egrep
parameters: []
features:
- file-system
- local
- pipes-stdin
execution:
  template: egrep
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: grep '' /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/egrep/
techniques:
- collection
install:
- method: apt
  package_name: grep
  commands:
  - apt-get install -y grep
---

# egrep

egrep is a command-line utility. Extended grep for pattern matching in files; can also read arbitrary files.
