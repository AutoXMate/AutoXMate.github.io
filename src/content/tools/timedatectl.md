---
id: system-time-timedatectl
namespace: system:time:timedatectl
name: timedatectl
description: Control system time and date settings; can spawn a shell.
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
- timedatectl
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
execution:
  template: timedatectl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Leverage less capabilities
  command: timedatectl list-timezones
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/timedatectl/
techniques:
- execution
install:
- method: apt
  package_name: systemd
  commands:
  - apt-get install -y systemd
---

# timedatectl

timedatectl is a command-line utility. Control system time and date settings Can leverage capabilities from: less.
