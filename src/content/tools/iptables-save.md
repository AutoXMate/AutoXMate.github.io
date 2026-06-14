---
id: network-firewall-iptables-save
namespace: network:firewall:iptables-save
name: iptables-save
description: Save iptables rules, can read files and execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.execution.command
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
  - iptables
  - ip6tables
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - iptables-save
  - iptables
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - process-manip
  - requires-root
execution:
  template: "iptables-save /path/to/file"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via iptables-save
    command: iptables-save /path/to/file
  - description: Execute command via iptables-save
    command: iptables-save /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/iptables-save/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "iptables"
    commands:
      - "apt-get install -y iptables"
---
