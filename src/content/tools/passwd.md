---
id: system-auth-passwd
namespace: system:auth:passwd
name: passwd
description: Change user password, can execute commands via helper programs.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - chsh
  - chfn
artifacts: []
workflow_edges:
  produces:
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - passwd
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "passwd /path/to/config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via passwd
    command: passwd /path/to/config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/passwd/"
techniques:
  - execution
install:
  - method: apt
    package_name: "passwd"
    commands:
      - "apt-get install -y passwd"
---
