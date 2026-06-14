---
id: system-daemon-systemd-run
namespace: system:daemon:systemd-run
name: systemd-run
description: Run commands in transient systemd services; can execute arbitrary commands
  and spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
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
- systemd-run
parameters: []
features:
- interactive
- pipes-stdin
- process-manip
- requires-root
execution:
  template: systemd-run
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo)
  command: systemd-run /path/to/command
- description: Spawn an interactive shell (sudo)
  command: systemd-run -S
- description: Spawn an interactive shell (sudo)
  command: systemd-run -t /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/systemd-run/
techniques:
- execution
- privilege-escalation
install:
- method: apt
  package_name: systemd
  commands:
  - apt-get install -y systemd
---

# systemd-run

systemd-run is a command-line utility. Run commands in transient systemd scopes/services.
