---
id: text-display-more
namespace: text:display:more
name: more
description: Pager, can read files and execute commands via ! command.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.privilege-escalation.shell
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
  - less
  - most
artifacts: []
workflow_edges:
  produces:
    - file-content
    - shell-access
  consumes:
    - file
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - more
  - less
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
  - process-manip
execution:
  template: "more /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via more
    command: more /path/to/file
  - description: Spawn a shell via more
    command: |
      more /path/to/file
      !/bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/more/"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
  - method: apt
    package_name: "util-linux"
    commands:
      - "apt-get install -y util-linux"
---
