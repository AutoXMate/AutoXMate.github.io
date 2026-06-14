---
id: network-dns-dnsmasq
namespace: network:dns:dnsmasq
name: dnsmasq
description: DNS forwarder and DHCP server, can execute commands via --conf-script
  option.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- linux
risk_level: high
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
  - command-execution
  consumes:
  - execution-context
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
- dnsmasq
- Bash
- execFile
parameters: []
features:
- requires-root
- process-manip
execution:
  template: dnsmasq --conf-script='/path/to/command 1>&2'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute a command via dnsmasq --conf-script
  command: dnsmasq --conf-script='/path/to/command 1>&2'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/dnsmasq/
techniques:
- execution
install:
- method: apt
  package_name: dnsmasq
  commands:
  - apt-get install -y dnsmasq
mitre_ids:
- T1046
- T1069
- T1592
---


