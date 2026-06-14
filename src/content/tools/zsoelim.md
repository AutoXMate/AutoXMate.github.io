---
id: system-text-zsoelim
namespace: system:text:zsoelim
name: zsoelim
description: "Resolve .so requests in compressed groff files; can read arbitrary files."
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
- zsoelim
parameters: []
features: []
execution:
  template: zsoelim
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: zsoelim /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zsoelim/
techniques:
- collection
install:
- method: apt
  package_name: groff
  commands:
  - apt-get install -y groff
---


# zsoelim

zsoelim is a command-line utility. Resolve .so requests in compressed groff files; can also read arbitrary files.
