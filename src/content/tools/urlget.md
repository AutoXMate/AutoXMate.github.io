---
id: network-transfer-urlget
namespace: network:transfer:urlget
name: urlget
description: Fetch URLs using uriparser library; can download and upload files.
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
- urlget
parameters: []
features:
- file-system
- local
- network-intensive
execution:
  template: urlget
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: urlget - /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/urlget/
techniques:
- collection
install:
- method: apt
  package_name: urlget
  commands:
  - apt-get install -y urlget
---

# urlget

urlget is a command-line utility. Fetch URLs using the uriparser library; can also read arbitrary files.
