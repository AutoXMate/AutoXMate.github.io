---
id: archive-pax-pax
namespace: archive:pax:pax
name: pax
description: Portable archive tool, can read and write files.
author: GTFOBins
version: 1.0.0
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
- tar
- cpio
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
- pax
- tar
- Bash
- execFile
parameters: []
features:
- file-system
execution:
  template: pax -r -s /path/to/input /path/to/output
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read a file via pax
  command: pax -r -s /path/to/input /path/to/output
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/pax/
techniques:
- collection
install:
- method: apt
  package_name: pax
  commands:
  - apt-get install -y pax
mitre_ids:
- T1560
---


