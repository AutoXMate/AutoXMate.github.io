---
id: document-convert-pandoc
namespace: document:convert:pandoc
name: pandoc
description: Document converter, can read files and execute commands via filters.
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
      description: File or command output
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
  - pandoc
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "pandoc /path/to/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via pandoc
    command: pandoc /path/to/file
  - description: Execute command via pandoc filter
    command: pandoc /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pandoc/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "pandoc"
    commands:
      - "apt-get install -y pandoc"
---
