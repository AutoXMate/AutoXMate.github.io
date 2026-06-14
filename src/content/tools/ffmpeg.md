---
id: multimedia-ffmpeg-ffmpeg
namespace: multimedia:ffmpeg:ffmpeg
name: ffmpeg
description: Multimedia converter, can read and write files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
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
related_tools: []
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
    cpu: medium
    memory_mb: 64
    network: none
    disk_io: medium
resource_profile:
  cpu: medium
  memory_mb: 64
  network: none
  disk_io: medium
allowed-tools:
  - ffmpeg
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "ffmpeg -i /path/to/input /path/to/output"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via ffmpeg
    command: ffmpeg -i /path/to/file
  - description: Write to a file via ffmpeg
    command: ffmpeg -i /path/to/input /path/to/output
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ffmpeg/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "ffmpeg"
    commands:
      - "apt-get install -y ffmpeg"
---
