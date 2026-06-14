---
id: system-daemon-start-stop-daemon
namespace: system:daemon:start-stop-daemon
name: start-stop-daemon
description: Start and stop system daemons; can spawn a shell.
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
- start-stop-daemon
parameters: []
features:
- compression
- file-system
- interactive
- process-manip
- requires-root
execution:
  template: start-stop-daemon
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: start-stop-daemon -S -x /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/start-stop-daemon/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: dpkg
  commands:
  - apt-get install -y dpkg
---

# start-stop-daemon

start-stop-daemon is a command-line utility. Start and stop system daemon programs; can also spawn an interactive shell.
