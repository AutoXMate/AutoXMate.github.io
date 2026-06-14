---
id: network-vpn-openvpn
namespace: network:vpn:openvpn
name: openvpn
description: OpenVPN client, can execute commands via config and up/down scripts.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
  - system.file.read
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
  - openvpn
  - Bash
  - execFile
parameters: []
features:
  - file-system
  - requires-root
  - process-manip
execution:
  template: "openvpn --config /path/to/config.ovpn"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Read a file via openvpn
    command: openvpn --config /path/to/file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/openvpn/"
techniques:
  - collection
  - execution
install:
  - method: apt
    package_name: "openvpn"
    commands:
      - "apt-get install -y openvpn"
---
