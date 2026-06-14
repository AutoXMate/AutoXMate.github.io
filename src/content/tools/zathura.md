---
id: system-pdf-zathura
namespace: system:pdf:zathura
name: zathura
description: Minimalistic PDF/document viewer; can read arbitrary files.
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
- zathura
parameters: []
features:
- file-system
- interactive
- local
- pipes-stdout
- requires-root
execution:
  template: zathura
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'zathura

    :! /bin/sh -c ''exec /bin/sh 0<&1'''
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zathura/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: zathura
  commands:
  - apt-get install -y zathura
---

# zathura

zathura is a command-line utility. Minimalistic PDF and document viewer; can also spawn an interactive shell.
