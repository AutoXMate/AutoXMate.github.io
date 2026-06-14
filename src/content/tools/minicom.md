---
id: system-terminal-minicom
namespace: system:terminal:minicom
name: minicom
description: Serial communication program, can read files and execute commands.
author: GTFOBins
version: 1.0.0
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
related_tools:
- screen
- picocom
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
- minicom
- Bash
- execFile
parameters: []
features:
- file-system
- interactive
- process-manip
execution:
  template: minicom /path/to/script
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read a file via minicom
  command: minicom /path/to/file
- description: Execute command via minicom
  command: minicom /path/to/script
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/minicom/
techniques:
- collection
- execution
install:
- method: apt
  package_name: minicom
  commands:
  - apt-get install -y minicom
mitre_ids:
- T1059
---


