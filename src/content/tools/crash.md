---
id: system-diagnostic-crash
namespace: system:diagnostic:crash
name: crash
description: Linux kernel crash dump analysis tool, can read files via pager and execute commands via CRASHPAGER.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
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
related_tools:
  - less
artifacts: []
workflow_edges:
  produces:
    - file-content
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command or file output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - crash
  - less
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "crash -h"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute a command via CRASHPAGER
    command: CRASHPAGER=/path/to/command crash -h
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/crash/"
techniques:
  - execution
install:
  - method: apt
    package_name: "crash"
    commands:
      - "apt-get install -y crash"
---
