---
id: system-x-xmodmap
namespace: system:x:xmodmap
name: xmodmap
description: Modifier key and pointer mapping in X11; can read arbitrary files.
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
- xmodmap
parameters: []
features:
- file-system
- local
- network-intensive
execution:
  template: xmodmap
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: xmodmap -v /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/xmodmap/
techniques:
- collection
install:
- method: apt
  package_name: x11-utils
  commands:
  - apt-get install -y x11-utils
---

# xmodmap

xmodmap is a command-line utility. Modifier key and pointer button mapping in X11; can also read arbitrary files.
