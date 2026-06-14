---
id: archive-zip-unzip
namespace: archive:zip:unzip
name: unzip
description: "Extract compressed ZIP archives; can read arbitrary files."
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
- unzip
parameters: []
features: []
execution:
  template: unzip
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Privilege-escalation (sudo, suid)
  command: 'unzip -K shell.zip

    ./sh -p'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/unzip/
techniques:
- execution
install:
- method: apt
  package_name: unzip
  commands:
  - apt-get install -y unzip
---


# unzip

unzip is a command-line utility. Extract compressed ZIP archives.
