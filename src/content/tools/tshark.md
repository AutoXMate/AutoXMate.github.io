---
id: network-sniff-tshark
namespace: network:sniff:tshark
name: tshark
description: Wireshark CLI network protocol analyzer; can spawn a shell.
author: GTFOBins
version: 1.0.0
capabilities:
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - shell-access
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- tshark
parameters: []
features:
- interactive
- network-intensive
- pipes-stdin
- process-manip
execution:
  template: tshark
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage lua capabilities
  command: 'echo ''...'' >/path/to/temp-file

    tshark -Xlua_script:/path/to/temp-file'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tshark/
techniques:
- execution
install:
- method: apt
  package_name: tshark
  commands:
  - apt-get install -y tshark
---

# tshark

tshark is a command-line utility. Wireshark command-line network protocol analyzer Can leverage capabilities from: lua.
