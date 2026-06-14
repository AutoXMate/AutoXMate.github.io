---
id: shell-bashbug
namespace: shell:bourne:bashbug
name: bashbug
description: Bash bug reporting tool that opens a vi editor, which can be used to execute commands.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - vi
  - vim
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell access via vi escape
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
  - bashbug
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "bashbug"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Open vi editor via bashbug, then use :!command to execute shell commands
    command: bashbug
references:
  - label: "bashbug man page"
    url: "https://man7.org/linux/man-pages/man1/bashbug.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "bash"
      commands:
        - "apt-get install -y bash"
---


# bashbug — Bash Bug Reporting Tool

bashbug is a shell script that reports bugs to the Bash maintainers. It opens a vi editor for writing the bug report, which can be abused to execute commands via `:!command` escape in vi.
