---
id: text-format-column
namespace: text:format:column
name: column
description: Columnate text input, can read files by formatting arbitrary file content.
author: GTFOBins
version: 1.0.0
capabilities:
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
    description: File content
  side_effects: []
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
- column
- Bash
- execFile
parameters:
- name: input
  type: file
  required: false
  description: File to read
features:
- file-system
- local
execution:
  template: column {input}
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read a file via column
  command: column /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/column/
techniques:
- collection
install:
- method: apt
  package_name: bsdmainutils
  commands:
  - apt-get install -y bsdmainutils
---


