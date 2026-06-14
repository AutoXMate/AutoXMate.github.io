---
id: text-tex-pdftex
namespace: text:tex:pdftex
name: pdftex
description: PDFTeX engine, can read files and execute commands.
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
related_tools:
  - pdflatex
  - tex
  - latex
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
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - pdftex
  - pdflatex
  - tex
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "pdftex /path/to/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via pdftex
    command: pdftex /path/to/file
  - description: Execute command via pdftex
    command: pdftex /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pdftex/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "texlive-base"
    commands:
      - "apt-get install -y texlive-base"
---
