---
id: text-highlight-pygmentize
namespace: text:highlight:pygmentize
name: pygmentize
description: Source code highlighter, can read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - macos
  - bsd
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - highlight
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
  - pygmentize
  - highlight
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "pygmentize /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via pygmentize
    command: pygmentize /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pygmentize/"
techniques:
  - collection
install:
  - method: pip
    package_name: "Pygments"
    commands:
      - "pip install Pygments"
---
