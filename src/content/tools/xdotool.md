---
id: system-x-xdotool
namespace: system:x:xdotool
name: xdotool
description: Simulate X11 keyboard/mouse input programmatically; can read arbitrary
  files.
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
- xdotool
parameters: []
features:
- file-system
- interactive
- local
- requires-root
execution:
  template: xdotool
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: xdotool exec --sync /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/xdotool/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: xdotool
  commands:
  - apt-get install -y xdotool
---

# xdotool

xdotool is a command-line utility. Programmatically simulate X11 keyboard/mouse input; can also spawn an interactive shell.
