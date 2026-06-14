---
id: network-arp
namespace: network:discovery:arp
name: arp
description: ARP table manipulation tool that can read files when used with privileges
  via -f flag.
author: Repository Maintainers
version: 1.0.0
capabilities:
- network.discovery.host
- network.arp.manipulate
- system.file.read
platforms:
- linux
- macos
- cross-platform
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- ip
- ifconfig
artifacts:
- type: network.arp.table
  description: ARP cache table
  mime: text/plain
  trust_level: community
workflow_edges:
  produces:
  - arp-table
  consumes: []
contract:
  inputs:
  - type: network.interface.name
    description: Network interface name
  outputs:
  - type: network.arp.table
    description: ARP cache entries
    mime: text/plain
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
- arp
- Bash
- execFile
parameters:
- name: f
  type: file
  required: false
  description: Read entries from file
  aliases:
  - -f
features:
- file-system
- local
- network-intensive
- pipes-stdin
- requires-root
execution:
  template: arp {f}
  sandbox: execFile
  timeout_seconds: 10
  shell: false
global_vars: {}
examples:
- description: Read arbitrary file parsed as ARP table entries via -f flag
  command: arp -f /path/to/input-file
references:
- label: arp man page
  url: https://man7.org/linux/man-pages/man8/arp.8.html
techniques:
- discovery
- collection
install:
- method: apt
  package_name: net-tools
  commands:
  - apt-get install -y net-tools
mitre_ids:
- T1012
- T1046
- T1082
- T1087
---

# arp — ARP Table Manager

arp displays and manipulates the system's ARP cache. When used with elevated privileges, the `-f` flag reads a file as ARP entries, which can leak file contents through error messages.
