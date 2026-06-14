---
id: runtime-node-node
namespace: runtime:node:node
name: node
description: JavaScript runtime, can execute JS code and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - npm
  - npx
  - yarn
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: JS execution output
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
  - node
  - npm
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: 'node -e "require(\"child_process\").execSync(\"/bin/sh\")"'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via node
    command: node -e 'require("child_process").execSync("/bin/sh")'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/node/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "nodejs"
    commands:
      - "apt-get install -y nodejs"
---
