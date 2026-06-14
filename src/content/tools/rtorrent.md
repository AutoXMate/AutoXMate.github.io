---
id: network-bittorrent-rtorrent
namespace: network:bittorrent:rtorrent
name: rtorrent
description: BitTorrent client, can read files and execute commands.
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
    - network_traffic
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
  - rtorrent
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - interactive
execution:
  template: "rtorrent /path/to/file"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via rtorrent
    command: rtorrent /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rtorrent/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "rtorrent"
    commands:
      - "apt-get install -y rtorrent"
---
