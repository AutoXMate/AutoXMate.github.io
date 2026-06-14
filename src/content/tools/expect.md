---
id: automation-expect
namespace: automation:interactive:expect
name: expect
description: Automates interactive applications, can read files and spawn interactive shells.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - system.file.read
  - security.privilege-escalation.shell
  - automation.script
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - file-content
    - shell-access
  consumes:
    - input-file
contract:
  inputs:
    - type: system.file.path
      description: Path to expect script
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - expect
  - Bash
  - execFile
parameters:
  - name: c
    type: string
    required: false
    description: "Command to execute"
    aliases:
      - -c
features:
  - process-manip
execution:
  template: "expect {c}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read arbitrary file via parsing error message
    command: expect /path/to/input-file
  - description: Spawn interactive shell
    command: expect -c 'spawn /bin/sh;interact'
  - description: Spawn privileged shell with SUID
    command: expect -c 'spawn /bin/sh -p;interact'
references:
  - label: "expect man page"
    url: "https://man7.org/linux/man-pages/man1/expect.1.html"
techniques:
  - privilege-escalation
  - execution
  - collection
install:
    - method: apt
      package_name: "expect"
      commands:
        - "apt-get install -y expect"
---


# expect — Programmed Dialogue with Interactive Programs

expect automates interactive applications. When used with sudo or SUID, it can read files through parsing errors and spawn interactive shells via the `spawn` and `interact` commands.
