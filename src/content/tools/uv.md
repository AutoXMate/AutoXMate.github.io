---
id: dev-python-uv
namespace: dev:python:uv
name: uv
description: "Fast Python package installer and resolver; can execute arbitrary code."
author: GTFOBins
version: 1.0.0
capabilities:
- security.privilege-escalation.shell
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
- uv
parameters: []
features: []
execution:
  template: uv
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: uv run /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/uv/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: uv
  commands:
  - apt-get install -y uv
---


# uv

uv is a command-line utility. Fast Python package installer and resolver; can also spawn an interactive shell.
