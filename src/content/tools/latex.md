---
id: text-tex-latex
namespace: text:tex:latex
name: latex
description: LaTeX typesetting, can read files via \input and execute commands.
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
  - lualatex
  - xelatex
  - pdflatex
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
  - latex
  - pdflatex
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "latex \\\\input{/path/to/file}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via latex
    command: latex '\input{/path/to/file}'
  - description: Execute command via latex
    command: latex '\input{/path/to/file}'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/latex/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "texlive-latex-base"
    commands:
      - "apt-get install -y texlive-latex-base"
---
