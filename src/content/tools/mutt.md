---
id: network-email-mutt
namespace: network:email:mutt
name: mutt
description: Terminal email client, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - mail
  - alpine
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
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - mutt
  - mail
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
  - process-manip
execution:
  template: "mutt -f /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via mutt
    command: mutt -f /path/to/file
  - description: Execute command via mutt
    command: mutt -f /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/mutt/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "mutt"
    commands:
      - "apt-get install -y mutt"
---
