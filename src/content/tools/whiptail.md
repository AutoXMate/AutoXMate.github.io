---
id: system-ui-whiptail
namespace: system:ui:whiptail
name: whiptail
description: "Display dialog boxes from shell scripts; can spawn a shell."
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
- whiptail
parameters: []
features: []
execution:
  template: whiptail
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: whiptail --textbox --scrolltext /path/to/input-file 0 0
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/whiptail/
techniques:
- collection
install:
- method: apt
  package_name: whiptail
  commands:
  - apt-get install -y whiptail
---


# whiptail

whiptail is a command-line utility. Display dialog boxes from shell scripts; can also read arbitrary files.
