---
id: dev-tcl-wish
namespace: dev:tcl:wish
name: wish
description: "Tcl/Tk GUI application shell; can inherit Tcl capabilities."
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
- wish
parameters: []
features: []
execution:
  template: wish
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage tclsh capabilities
  command: wish
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/wish/
techniques:
- execution
install:
- method: apt
  package_name: tk
  commands:
  - apt-get install -y tk
---


# wish

wish is a command-line utility. Tcl/Tk GUI application shell; can leverage tclsh capabilities Can leverage capabilities from: tclsh.
