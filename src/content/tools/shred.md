---
id: system-file-shred
namespace: system:file:shred
name: shred
description: "Securely delete files by overwriting them multiple times."
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.write
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
- shred
parameters: []
features: []
execution:
  template: shred
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Write to arbitrary files (sudo, suid, unprivileged)
  command: shred -u /path/to/output-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/shred/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: coreutils
  commands:
  - apt-get install -y coreutils
---


# shred

shred is a command-line utility. Securely delete files by overwriting them; can also write to arbitrary files.
