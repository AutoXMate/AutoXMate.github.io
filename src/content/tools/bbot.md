---
id: security-recon-bbot
namespace: security:recon:bbot
name: bbot
description: OSINT reconnaissance tool, can read files via debug log output.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
platforms:
- linux
risk_level: low
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
    description: File content in debug log
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- bbot
- Bash
- execFile
parameters:
- name: input
  type: file
  required: false
  description: File to read
features:
- file-system
execution:
  template: bbot -d -cy {input}
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read a file via bbot debug log
  command: bbot -d -cy /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/bbot/
techniques:
- collection
install:
- method: pip
  package_name: bbot
  commands:
  - pip install bbot
items:
- NoCreds
services:
- DNS
- HTTP
mitre_ids:
- T1046
- T1595
---


