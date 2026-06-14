---
id: text-tex-latexmk
namespace: text:tex:latexmk
name: latexmk
description: LaTeX build tool, can execute commands via latex engine.
author: "GTFOBins"
version: "1.0.0"
capabilities:
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
  - latex
  - pdflatex
artifacts: []
workflow_edges:
  produces:
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command output
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
  - latexmk
  - latex
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "latexmk /path/to/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via latexmk
    command: latexmk /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/latexmk/"
techniques:
  - execution
install:
  - method: apt
    package_name: "latexmk"
    commands:
      - "apt-get install -y latexmk"
---
