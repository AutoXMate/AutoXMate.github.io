---
id: lang-scheme-ginsh
namespace: lang:scheme:ginsh
name: ginsh
description: GiNaC symbolic math shell, can execute commands and read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
      description: File or command output
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
  - ginsh
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "ginsh < /path/to/script"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via ginsh
    command: ginsh < /path/to/script
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ginsh/"
techniques:
  - execution
  - collection
install:
  - method: apt
    package_name: "ginac-tools"
    commands:
      - "apt-get install -y ginac-tools"
---
