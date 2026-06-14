---
id: cache-redis-redis
namespace: cache:redis:redis
name: redis
description: Redis CLI, can execute commands and read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Redis command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - redis
  - redis-cli
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "redis-cli -h host eval /path/to/script"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via redis
    command: redis-cli -h host eval /path/to/script
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/redis/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "redis-tools"
    commands:
      - "apt-get install -y redis-tools"
---
