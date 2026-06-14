---
id: document-pdf-qpdf
namespace: document:pdf:qpdf
name: qpdf
description: PDF manipulation tool, can read and write files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
platforms:
  - linux
  - bsd
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - pdftk
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects:
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
  - qpdf
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "qpdf /path/to/input /path/to/output"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via qpdf
    command: qpdf /path/to/input /path/to/output
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/qpdf/"
techniques:
  - collection
install:
  - method: apt
    package_name: "qpdf"
    commands:
      - "apt-get install -y qpdf"
---
