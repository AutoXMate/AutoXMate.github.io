---
id: web-browser-w3m
namespace: web:browser:w3m
name: w3m
description: Text-based web browser; can read arbitrary files.
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
- w3m
parameters: []
features:
- file-system
- local
- pipes-stdin
execution:
  template: w3m
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: w3m -dump /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/w3m/
techniques:
- collection
install:
- method: apt
  package_name: w3m
  commands:
  - apt-get install -y w3m
---

# w3m

w3m is a command-line utility. Text-based web browser; can also read arbitrary files.
