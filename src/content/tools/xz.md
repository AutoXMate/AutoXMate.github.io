---
id: compression-xz-xz
namespace: compression:xz:xz
name: xz
description: General-purpose data compression utility; can read arbitrary files.
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
- xz
parameters: []
features:
- compression
- file-system
- local
execution:
  template: xz
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: xz -c /path/to/input-file | xz -d
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/xz/
techniques:
- collection
install:
- method: apt
  package_name: xz-utils
  commands:
  - apt-get install -y xz-utils
mitre_ids:
- T1560
---

# xz

xz is a command-line utility. General-purpose data compression utility; can also read arbitrary files.
