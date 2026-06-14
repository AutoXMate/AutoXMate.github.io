---
id: process-lock-flock
namespace: process:lock:flock
name: flock
description: Manage file locks from shell scripts, can spawn a shell when used with privileges.
author: "Repository Maintainers"
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
    memory_mb: 2
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: low
  disk_io: low
allowed-tools:
  - flock
  - Bash
  - execFile
parameters:
  - name: u
    type: string
    required: false
    description: "Unlock a file descriptor"
    aliases:
      - -u
features:
  - process-manip
execution:
  template: "flock {u}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell via flock unlock
    command: flock -u / /bin/sh
  - description: Spawn privileged shell with SUID
    command: flock -u / /bin/sh -p
references:
  - label: "flock man page"
    url: "https://man7.org/linux/man-pages/man1/flock.1.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "util-linux"
      commands:
        - "apt-get install -y util-linux"
---


# flock — File Lock Manager

flock manages file locks from shell scripts. The `-u /` flag unlocks the root filesystem and can spawn a shell, useful for privilege escalation when used with sudo or SUID.
