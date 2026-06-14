---
id: network-email-mail
namespace: network:email:mail
name: mail
description: GNU mail processor that can spawn a shell via exec flag or mail interactive mode.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - network.email.client
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
  - alpine
  - mutt
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
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
  - mail
  - Bash
  - execFile
parameters:
  - name: exec
    type: string
    required: false
    description: "Execute command after processing"
    aliases:
      - --exec
  - name: f
    type: file
    required: false
    description: "Read mailbox from file"
    aliases:
      - -f
features:
  - process-manip
execution:
  template: "mail {exec} {f}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell via --exec flag
    command: mail --exec='!/bin/sh'
  - description: Spawn shell via interactive mail command
    command: |-
      mail -f /etc/hosts
      !/bin/sh
references:
  - label: "mailx man page"
    url: "https://man7.org/linux/man-pages/man1/mailx.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "mailutils"
      commands:
        - "apt-get install -y mailutils"
---


# mail — GNU Mail Processor

mail reads and sends email. The GNU version can execute shell commands via the `--exec` flag or from the interactive prompt with `!`. Useful for privilege escalation when used with sudo or SUID.
