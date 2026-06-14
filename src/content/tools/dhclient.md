---
id: network-dhcp-dhclient
namespace: network:dhcp:dhclient
name: dhclient
description: DHCP client, can spawn a shell via the -sf (shell script) option.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
    - shell-access
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
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
  - dhclient
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "dhclient -sf /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via dhclient -sf
    command: dhclient -sf /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dhclient/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "isc-dhcp-client"
    commands:
      - "apt-get install -y isc-dhcp-client"
---
