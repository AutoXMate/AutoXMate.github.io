---
id: text-tex-lualatex
namespace: text:tex:lualatex
name: lualatex
description: LuaLaTeX typesetting, can read files and execute Lua code.
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
  - latex
  - luatex
  - tex
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
  - lualatex
  - luatex
  - latex
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "lualatex /path/to/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via lualatex
    command: lualatex /path/to/file
  - description: Execute Lua code via lualatex
    command: lualatex /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/lualatex/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "texlive-luatex"
    commands:
      - "apt-get install -y texlive-luatex"
---
