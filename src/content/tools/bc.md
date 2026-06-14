---
id: math-bc
namespace: math:calc:bc
name: bc
description: Arbitrary precision calculator language that can read files via -s flag, leaking content as errors.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - math.calculate
platforms:
  - linux
  - macos
  - cross-platform
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
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to read
  outputs:
    - type: system.file.content
      description: File content leaked as error messages
      mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - bc
  - Bash
  - execFile
parameters:
  - name: s
    type: string
    required: false
    description: "Load file and suppress normal output"
    aliases:
      - -s
features: []
execution:
  template: "bc {s}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via -s flag, content appears as error messages
    command: |-
      bc -s /path/to/input-file
      quit
references:
  - label: "bc man page"
    url: "https://man7.org/linux/man-pages/man1/bc.1.html"
techniques:
  - collection
install:
    - method: apt
      package_name: "bc"
      commands:
        - "apt-get install -y bc"
---


# bc — Calculator Language

bc is an arbitrary precision calculator language. The `-s` flag loads a file for processing, and its content appears in error messages when parsing fails, making it useful for file read when used with elevated privileges.
