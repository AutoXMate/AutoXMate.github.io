---
id: security-antivirus-clamscan
namespace: security:antivirus:clamscan
name: clamscan
description: ClamAV antivirus scanner, can read files via error message leakage with custom YARA rules.
author: "GTFOBins"
version: "1.0.0"
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
      description: File content in error messages
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
  - clamscan
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to read"
features:
  - file-system
execution:
  template: "clamscan --no-summary -d x.yara -f {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via clamscan error message leakage
    command: |
      touch x.yara
      clamscan --no-summary -d x.yara -f /path/to/input-file 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/clamscan/"
techniques:
  - collection
install:
  - method: apt
    package_name: "clamav"
    commands:
      - "apt-get install -y clamav"
items:
  - NoCreds
services:
  - HTTP
---
