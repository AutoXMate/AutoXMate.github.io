---
id: backup-bareos-bconsole
namespace: backup:bareos:bconsole
name: bconsole
description: Bareos backup console, can read files via error messages and spawn shells via @exec.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or SUID execution context
  outputs:
    - type: process.output
      description: Shell or file content output
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
  - bconsole
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read or config to parse"
  - name: exec_cmd
    type: string
    required: false
    description: "Command to execute via @exec"
features:
  - interactive
  - process-manip
execution:
  template: "bconsole"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via bconsole error message
    command: bconsole -c /path/to/file-input
  - description: Spawn a shell from the bconsole CLI
    command: |
      bconsole
      @exec /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/bconsole/"
techniques:
  - collection
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "bareos-console"
    commands:
      - "apt-get install -y bareos-console"
---
