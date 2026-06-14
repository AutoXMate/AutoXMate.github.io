---
id: system-notes-xpad
namespace: system:notes:xpad
name: xpad
description: "Sticky note application for X11; can read arbitrary files."
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
- xpad
parameters: []
features: []
execution:
  template: xpad
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: xpad -f /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/xpad/
techniques:
- collection
install:
- method: apt
  package_name: xpad
  commands:
  - apt-get install -y xpad
---


# xpad

xpad is a command-line utility. Sticky note application for X11; can also read arbitrary files.
