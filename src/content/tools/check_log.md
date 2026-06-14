---
id: monitoring-nagios-check-log
namespace: monitoring:nagios:check-log
name: check_log
description: Nagios plugin for log file checking, can read and write files via -F/-O options.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
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
    - file-content
  consumes:
    - file
contract:
  inputs:
    - type: system.file.path
      description: Path to input file
  outputs:
    - type: process.output
      description: File content output
  side_effects:
    - process_spawn
    - filesystem_write
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
  - check_log
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read"
  - name: output
    type: file
    required: false
    description: "File to write"
features:
  - file-system
execution:
  template: "check_log -F {input} -O {output}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via check_log
    command: check_log -F /path/to/input-file -O /dev/stdout
  - description: Write to a file via check_log
    command: check_log -F /path/to/input-file -O /path/to/output-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/check_log/"
techniques:
  - collection
  - exfiltration
install:
  - method: apt
    package_name: "monitoring-plugins"
    commands:
      - "apt-get install -y monitoring-plugins"
---
