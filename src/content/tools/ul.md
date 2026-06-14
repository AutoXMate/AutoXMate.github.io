---
id: system-text-ul
namespace: system:text:ul
name: ul
description: "Underline text for terminals; can read arbitrary files."
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
- ul
parameters: []
features: []
execution:
  template: ul
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: ul /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ul/
techniques:
- collection
install:
- method: apt
  package_name: bsdmainutils
  commands:
  - apt-get install -y bsdmainutils
---


# ul

ul is a command-line utility. Underline text for terminals; can also read arbitrary files.
