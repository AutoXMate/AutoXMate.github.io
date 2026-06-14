---
id: system-log-rsyslogd
namespace: system:log:rsyslogd
name: rsyslogd
description: System logging daemon, can execute commands via config.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
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
  - rsyslogd
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "rsyslogd -f /path/to/config"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via rsyslogd
    command: rsyslogd -f /path/to/config
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rsyslogd/"
techniques:
  - execution
install:
  - method: apt
    package_name: "rsyslog"
    commands:
      - "apt-get install -y rsyslog"
---
