---
id: text-process-csvtool
namespace: text:process:csvtool
name: csvtool
description: CSV manipulation tool, can read/write files and spawn shells via call command.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
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
  inputs: []
  outputs:
    - type: process.output
      description: Shell or file output
  side_effects:
    - process_spawn
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - csvtool
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "csvtool call '/bin/sh;false' {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via csvtool call
    command: csvtool call '/bin/sh;false' /etc/hosts
  - description: Read a file via csvtool
    command: csvtool trim t /path/to/input-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/csvtool/"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
  - method: apt
    package_name: "csvtool"
    commands:
      - "apt-get install -y csvtool"
---
