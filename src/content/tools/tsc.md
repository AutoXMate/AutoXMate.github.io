---
id: dev-typescript-tsc
namespace: dev:typescript:tsc
name: tsc
description: TypeScript compiler; can execute code and spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
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
- tsc
parameters: []
features:
- file-system
- interactive
- local
- pipes-stdin
- process-manip
execution:
  template: tsc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, unprivileged)
  command: tsc /path/to/input-file.ts
- description: Write to arbitrary files (sudo, unprivileged)
  command: tsc /path/to/input-file.ts --outFile /path/to/output-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tsc/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: node-typescript
  commands:
  - apt-get install -y node-typescript
---

# tsc

tsc is a command-line utility. TypeScript compiler; can also read arbitrary files, write to arbitrary files.
