---
id: shell-ash
namespace: shell:bourne:ash
name: ash
description: Almquist shell, a lightweight Unix shell that can write files and spawn interactive shells.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
  - system.file.write
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
  - bash
  - sh
  - dash
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-output
    - file-content
  consumes: []
contract:
  inputs: []
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
  - ash
  - Bash
  - execFile
parameters:
  - name: c
    type: string
    required: false
    description: "Command to execute"
    aliases:
      - -c
  - name: p
    type: string
    required: false
    description: "Privileged mode (no profile files)"
    aliases:
      - -p
features:
  - process-manip
execution:
  template: "ash {c}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell
    command: ash
  - description: Spawn privileged interactive shell (SUID)
    command: ash -p
  - description: Write arbitrary data to file
    command: ash -c 'echo DATA >/path/to/output-file'
references:
  - label: "ash man page"
    url: "https://man7.org/linux/man-pages/man1/ash.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "busybox"
      commands:
        - "apt-get install -y busybox"
---


# ash — Almquist Shell

ash is a lightweight Unix shell commonly used in embedded systems and as /bin/sh on some BSD systems. When installed with SUID, it can spawn a privileged shell with `-p` flag.
