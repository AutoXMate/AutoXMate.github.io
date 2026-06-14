---
id: system-x-xmore
namespace: system:x:xmore
name: xmore
description: X11 text file browser; can read arbitrary files.
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
- xmore
parameters: []
features:
- file-system
- local
execution:
  template: xmore
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: xmore /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/xmore/
techniques:
- collection
install:
- method: apt
  package_name: x11-utils
  commands:
  - apt-get install -y x11-utils
---

# xmore

xmore is a command-line utility. X11 text file browser; can also read arbitrary files.
