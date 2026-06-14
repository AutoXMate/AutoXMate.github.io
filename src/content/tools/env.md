---
id: process-env
namespace: process:environment:env
name: env
description: Run a program in a modified environment, can spawn a shell.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
  - macos
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - nohup
  - nice
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
contract:
  inputs:
    - type: system.command.string
      description: Command to execute
  outputs:
    - type: process.output
      description: Command output
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
  - env
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "env {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive shell
    command: env /bin/sh
  - description: Spawn a privileged shell with SUID
    command: env /bin/sh -p
references:
  - label: "env man page"
    url: "https://man7.org/linux/man-pages/man1/env.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "coreutils"
      commands:
        - "apt-get install -y coreutils"
---


# env — Run in Modified Environment

env runs a program with modified environment variables. When installed with SUID, it can spawn a privileged shell with the `-p` flag.
