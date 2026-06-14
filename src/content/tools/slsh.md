---
id: dev-lang-slsh
namespace: dev:lang:slsh
name: slsh
description: S-Lang scripting language interpreter; can execute commands and spawn
  shells.
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
- slsh
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
- requires-root
execution:
  template: slsh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: slsh -e 'system("/bin/sh")'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/slsh/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: slsh
  commands:
  - apt-get install -y slsh
---

# slsh

slsh is a command-line utility. S-Lang scripting language interpreter; can also spawn an interactive shell.
