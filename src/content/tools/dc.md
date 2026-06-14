---
id: math-dc
namespace: math:calc:dc
name: dc
description: Reverse-polish desk calculator that can execute shell commands via the ! operator.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - math.calculate
platforms:
  - linux
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - bc
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
contract:
  inputs:
    - type: system.command.string
      description: Command to execute via dc -e
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - dc
  - Bash
  - execFile
parameters:
  - name: e
    type: string
    required: false
    description: "Evaluate expression"
    aliases:
      - -e
features:
  - process-manip
execution:
  template: "dc {e}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell via dc -e with ! operator
    command: dc -e '!/bin/sh'
references:
  - label: "dc man page"
    url: "https://man7.org/linux/man-pages/man1/dc.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "dc"
      commands:
        - "apt-get install -y dc"
---


# dc — Desk Calculator

dc is a reverse-polish desk calculator. The `!` operator executes shell commands, making it useful for privilege escalation when used with sudo or SUID.
