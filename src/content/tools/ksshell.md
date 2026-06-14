---
id: dev-kickstart-ksshell
namespace: dev:kickstart:ksshell
name: ksshell
description: Kickstart script parser; can read arbitrary files.
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
- ksshell
parameters: []
features:
- compression
- file-system
- interactive
- local
- network-intensive
execution:
  template: ksshell
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: ksshell -i /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ksshell/
techniques:
- collection
install:
- method: apt
  package_name: pykickstart
  commands:
  - apt-get install -y pykickstart
---

# ksshell

ksshell is a command-line utility. Kickstart script interpreter; can also read arbitrary files.
