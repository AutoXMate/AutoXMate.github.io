---
id: network-transfer-lftp
namespace: network:transfer:lftp
name: lftp
description: Sophisticated file transfer program, can download and upload files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - network.transfer.download
  - network.transfer.upload
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
  - curl
  - wget
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
    - network_traffic
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
  - lftp
  - curl
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
execution:
  template: "lftp -c 'get /path/to/remote/file'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Download a file via lftp
    command: lftp -c 'get /path/to/remote/file'
  - description: Upload a file via lftp
    command: lftp -c 'put /path/to/local/file'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/lftp/"
techniques:
  - exfiltration
  - collection
  - execution
install:
  - method: apt
    package_name: "lftp"
    commands:
      - "apt-get install -y lftp"
---
