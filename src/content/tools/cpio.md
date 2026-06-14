---
id: system-archive-cpio
namespace: system:archive:cpio
name: cpio
description: Copy files to and from archives, can read/write files and spawn shells via rsh-command.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
  - security.privilege-escalation.shell
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - tar
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File or shell output
  side_effects:
    - process_spawn
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
  - cpio
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "cpio"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via cpio
    command: echo /path/to/input-file | cpio -o
  - description: Spawn a shell via cpio rsh-command
    command: |
      echo '/bin/sh </dev/tty >/dev/tty' >localhost
      cpio -o --rsh-command /bin/sh -F localhost:
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cpio/"
techniques:
  - collection
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "cpio"
    commands:
      - "apt-get install -y cpio"
---
