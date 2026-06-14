---
id: text-process-join
namespace: text:process:join
name: join
description: Join lines of files on a common field, can read files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - bsd
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
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects: []
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
  - join
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "join /path/to/file1 /path/to/file2"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read files via join
    command: join /path/to/file1 /path/to/file2
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/join/"
techniques:
  - collection
install:
  - method: apt
    package_name: "coreutils"
    commands:
      - "apt-get install -y coreutils"
---
